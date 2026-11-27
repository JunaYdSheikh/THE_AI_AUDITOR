# AI Governance & Compliance Auditor (Mini-GRC Tool)

## Overview
This Python script is a proof-of-concept tool designed to perform automated compliance checks on AI decision logs and outputs. It translates AI governance policies (inspired by NIST AI RMF and EU AI Act transparency requirements) into automated control tests.

## The Problem it Solves
Organizations are deploying AI, but they lack continuous monitoring. Auditing AI manually is impossible. This tool acts as a "Policy-as-Code" mechanism to flag risk.

## Features
1. **Log Completeness Check:** Verifies that AI decisions contain required audit trails (timestamp, model version, user ID).
2. **Confidence Threshold Checking:** Flags any AI decision with a confidence score below 75% for mandatory Human-in-the-Loop (HITL) review.
3. **Bias/Claim Screening:** Scans AI-generated text for restricted absolute terms (e.g., "100% safe") that violate transparency standards.

## How to Run It
1. Ensure you have Python installed.
2. Clone this repository.
3. Run `python ai_auditor.py`

## Future Enhancements
- Connect to a real database instead of hardcoded JSON.
- Implement EU AI Act Article 50 (Transparency) logging requirements.
- Add a dashboard using Streamlit to visualize risk.