# Microsoft-Hackathon

# Zero-Knowledge Age Verifier using Flask and Azure Form Recognizer

## Overview

This project implements a privacy-focused age verification system by combining artificial intelligence with cryptographic techniques.

The system enables users to prove they are over 18 years of age without disclosing their actual date of birth. This is achieved through a simulated zero-knowledge proof (ZKP) model. The proof verifies an age-related claim while ensuring that sensitive personal information remains hidden.

This model serves as a foundation for building applications that align with data privacy regulations and principles such as GDPR, self-sovereign identity, and minimal disclosure.



## Concept

This application addresses the question:

"Can someone prove they are over 18 without revealing their actual date of birth?"

The system accepts an image of a government-issued identity document (such as a passport or driver’s license). Using Azure's Form Recognizer, it extracts structured fields including the date of birth. From this, it computes the individual's age and classifies the result as either:

- "Over 18"
- or
- "Under 18"

The classification is then hashed using SHA-256 to generate a cryptographic proof. This proof can be shared or verified without exposing the actual birth date. While this implementation is a simplified simulation, it models how zero-knowledge principles can be applied to real-world verification workflows.



## How It Works

1. A user uploads an image or PDF of their ID document.
2. The application uses Azure's `prebuilt-idDocument` model to extract structured data from the document.
3. The date of birth field is identified and extracted.
4. The system calculates the user's age using a static year (2025 in this prototype).
5. Based on the calculated age, it determines if the user is over or under 18.
6. The claim is hashed using the SHA-256 algorithm to generate a cryptographic proof.
7. The API returns a JSON response with the plain-text claim and its corresponding hash.


