# Microsoft-Hackathon

# Zero-Knowledge Age Verification using Flask and Azure Form Recognizer

## Overview

This project demonstrates a privacy-preserving age verification system built using Flask and Microsoft Azure's Form Recognizer service. The core idea is to verify whether a person is over 18 years old without exposing or storing their actual date of birth.

The concept simulates a form of zero-knowledge proof (ZKP), where the user can prove a statement ("I am over 18") without revealing the underlying data (their exact birth date). This approach is particularly relevant in systems where data minimization and privacy compliance (e.g., GDPR) are priorities.

---

## How It Works

1. The user uploads a scanned or photographed image of an official ID document (e.g., driver's license, passport).
2. The application uses Azure’s `prebuilt-idDocument` model to extract structured data from the document, including the date of birth.
3. It calculates the user’s age based on the current year (set to 2025 for this prototype).
4. If the user is 18 or older, the claim `"Over 18"` is created. If not, the claim is `"Under 18"`.
5. This claim is then hashed using the SHA-256 algorithm to create a verifiable cryptographic proof.
6. The application returns both the claim and its hashed proof in the response.

This allows external systems to trust the claim without accessing or storing the user's full date of birth.

---

## API Endpoint

### `POST /verify`

Accepts a form-data request containing an uploaded ID document file.

**Form-data Parameters:**

- `file`: Required. The image or PDF file of the ID document to be processed.

---

## Example Request

**Form Data:**
