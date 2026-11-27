import json
import re
from datetime import datetime

# ==========================================
# 1. THE POLICY CONFIGURATION (Governance)
# ==========================================
# In real GRC, rules come from a framework like NIST AI RMF or EU AI Act.
# We are defining our "Policy" here.
POLICY_RULES = {
    "required_log_fields": ["timestamp", "user_id", "model_version", "decision", "confidence_score"],
    "min_confidence_score": 0.75,
    "restricted_terms": ["guaranteed", "100% safe", "no risk", "perfect"] # AI should not make absolute claims
}

# ==========================================
# 2. THE AUDIT FUNCTIONS (Control Testing)
# ==========================================
def check_log_compliance(log_data):
    """Checks if the AI's decision log meets our governance policy."""
    print(f"\n--- Auditing Log: {log_data.get('log_id', 'Unknown')} ---")
    issues_found = 0
    
    # Test 1: Are all required fields present? (Completeness Check)
    for field in POLICY_RULES["required_log_fields"]:
        if field not in log_data:
            print(f"[FAIL] Missing required log field: {field}")
            issues_found += 1
            
    # Test 2: Is the confidence score above our risk threshold? (Risk Check)
    if "confidence_score" in log_data:
        if log_data["confidence_score"] < POLICY_RULES["min_confidence_score"]:
            print(f"[FAIL] Confidence score ({log_data['confidence_score']}) is below policy minimum ({POLICY_RULES['min_confidence_score']}). Flag for Human Review.")
            issues_found += 1
            
    if issues_found == 0:
        print("[PASS] Log is fully compliant with policy.")
    return issues_found

def check_text_bias(text_to_audit):
    """Scans AI-generated text for restricted, overly-promising language."""
    print("\n--- Auditing AI Output Text ---")
    issues_found = 0
    
    for term in POLICY_RULES["restricted_terms"]:
        if term.lower() in text_to_audit.lower():
            print(f"[FAIL] Non-compliant absolute claim found: '{term}'")
            issues_found += 1
            
    if issues_found == 0:
        print("[PASS] Text passes bias/risk screening.")
    return issues_found

# ==========================================
# 3. RUNNING THE AUDIT (Simulated Data)
# ==========================================
if __name__ == "__main__":
    print("Starting AI Governance Audit...")

    # Fake Data 1: A good, compliant AI decision
    good_log = {
        "log_id": "001",
        "timestamp": "2026-11-27T10:00:00Z",
        "user_id": "user_99",
        "model_version": "v1.2",
        "decision": "APPROVED",
        "confidence_score": 0.92
    }

    # Fake Data 2: A bad, non-compliant AI decision
    bad_log = {
        "log_id": "002",
        "timestamp": "2026-11-27T10:05:00Z",
        "user_id": "user_100",
        # Missing model_version
        "decision": "REJECTED",
        "confidence_score": 0.60 # Below 0.75 threshold
    }

    # Fake AI Text Output
    ai_text = "Our new loan algorithm is 100% safe and guaranteed to approve perfect candidates."

    # Run the tests
    check_log_compliance(good_log)
    check_log_compliance(bad_log)
    check_text_bias(ai_text)
    
    # Generate Audit Report
    print("\n=== FINAL AUDIT REPORT ===")
    print(f"Audit Date: {datetime.now().strftime('%Y-%m-%d')}")
    print("Status: Completed. See failures above for remediation.")