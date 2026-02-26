import pandas as pd
import joblib
import numpy as np
from urllib.parse import urlparse
import os

# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct paths
MODEL_PATH = os.path.join(BASE_DIR, "phishing_model_dataset_full.pkl")
SAFE_URLS_PATH = os.path.join(BASE_DIR, "balanced_urls.csv")

# Load model and safe URLs
model = joblib.load(MODEL_PATH)
safe_df = pd.read_csv(SAFE_URLS_PATH)
safe_urls = set(safe_df["url"].str.strip().str.lower())


def extract_features_from_url(url, domain, path	, query):
    features = [
        url.count('.'), url.count('-'), url.count('_'), url.count('/'), url.count('?'),
        url.count('='), url.count('@'), url.count('&'), url.count('!'), url.count(' '),
        url.count('~'), url.count(','), url.count('+'), url.count('*'), url.count('#'),
        url.count('$'), url.count('%'), len(domain.split('.')[-1]), len(url),
        domain.count('.'), domain.count('-'), domain.count('_'), domain.count('/'), domain.count('?'),
        domain.count('='), domain.count('@'), domain.count('&'), domain.count('!'), domain.count(' '),
        domain.count('~'), domain.count(','), domain.count('+'), domain.count('*'), domain.count('#'),
        domain.count('$'), domain.count('%'), sum(domain.count(v) for v in 'aeiou'), len(domain)
    ]
    while len(features) < 111:
        features.append(0)
    return np.array([features])

def check_url(url):
    url = url.strip().lower()
    url_for_check = url if url.startswith("http") else "http://" + url
    parsed = urlparse(url_for_check)
    domain = parsed.netloc
    path = parsed.path
    query = parsed.query

    features = extract_features_from_url(url_for_check, domain, path, query)
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0][prediction] * 100
    is_known_safe = url.rstrip('/') in safe_urls

    if is_known_safe and confidence < 80:
        return {"label": 1, "message": "Safe (Known trusted site, low phishing confidence)", "confidence": round(confidence, 2)}
    elif not is_known_safe and prediction == 1 and confidence >= 80:
        return {"label": 0, "message": "Phishing (High confidence)", "confidence": round(confidence, 2)}
    else:
        return {"label": 1, "message": "Safe", "confidence": round(confidence, 2)}

if __name__ == "__main__":
    print("🔍 AI-Powered Phishing URL Detector")
    print("-----------------------------------")
    
    if len(sys.argv) > 1:
        input_url = sys.argv[1]
    else:
        input_url = input("Enter URL to scan: ").strip()

    if input_url:
        result = check_url(input_url)
        print("\n--- Scan Result ---")
        print(f"Label      : {result['label']}")
        print(f"Confidence : {result['confidence']}%")
        print(f"Message    : {result['message']}")
    else:
        print("No URL entered. Exiting...")