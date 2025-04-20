# Microsoft-Hackathon

# 🔐 Zero-Knowledge Age Verifier using Flask + Azure Form Recognizer

## 📘 Overview

This project is a **privacy-preserving age verification system** that leverages AI and cryptographic techniques.

Instead of storing or exposing a person's **Date of Birth (DOB)**, it uses a simulated **Zero-Knowledge Proof (ZKP)** to confirm if the person is **over 18** — without ever revealing their actual DOB. This concept is crucial in building systems that protect sensitive user data while still enabling verifiable claims.

---

## 💡 Concept

> "Can you prove you're over 18 **without** telling me your birthday?"

The app accepts an image of an identity document (like a passport or license), uses **Azure Form Recognizer** to extract structured fields (like DOB), calculates the age, and returns a hashed proof of the statement:

- "Over 18"
- or
- "Under 18"

This hash acts as a **proof** of the claim. In a production-grade setup, this can be integrated with blockchain or digital ID platforms.

---

## ⚙️ How It Works

1. User uploads an image/PDF of their ID document.
2. The app uses Azure's `prebuilt-idDocument` model to extract fields.
3. It isolates the `DateOfBirth` field.
4. Calculates the current age (as of year 2025).
5. Generates a **SHA256 hash** of the claim: `"Over 18"` or `"Under 18"`.
6. Returns both the claim and its hashed proof in JSON format.

---

## 🚀 Running the App

Ensure you have:
- Flask installed
- Azure Form Recognizer endpoint set up
- Azure credentials set via environment (for `DefaultAzureCredential`)

```bash
python app.py
