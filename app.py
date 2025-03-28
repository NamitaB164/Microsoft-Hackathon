from flask import Flask, request, jsonify
import hashlib
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.identity import DefaultAzureCredential

app = Flask(__name__)

# Azure Form Recognizer Configuration
FORM_RECOGNIZER_ENDPOINT = "https://csai-docintel-20251111111.cognitiveservices.azure.com/"
FORM_RECOGNIZER_KEY = "6qg9czm5aLJP7j4epjTN44aCvHFrfH2PoRS49whwY9PEicQ7i4UTJQQJ99BCACL93NaXJ3w3AAALACOGbJDo"
document_client = DocumentAnalysisClient(FORM_RECOGNIZER_ENDPOINT, DefaultAzureCredential())

# Zero-Knowledge Proof (Basic Hashing Approach for PoC)
def generate_zkp(dob):
    age = 2025 - int(dob.split('-')[0])  # Extract year and calculate age
    claim = "Over 18" if age >= 18 else "Under 18"
    proof = hashlib.sha256(claim.encode()).hexdigest()
    return proof, claim

@app.route('/verify', methods=['POST'])
def verify():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    
    # Process the image through Form Recognizer
    poller = document_client.begin_analyze_document("prebuilt-idDocument", file.read())
    result = poller.result()
    
    # Extract DOB
    dob = None
    for field in result.documents[0].fields.values():
        if field.name == "DateOfBirth":
            dob = field.value
            break
    
    if not dob:
        return jsonify({"error": "DOB not found"}), 400
    
    proof, claim = generate_zkp(dob)
    return jsonify({"proof": proof, "claim": claim})

if __name__ == '__main__':
    app.run(debug=True)