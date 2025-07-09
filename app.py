from flask import Flask, render_template, request, jsonify
import joblib
from feature_extractor import extract_features
import os
from urllib.parse import urlparse

app = Flask(__name__)

# Load model
model = joblib.load("phishing_model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        # Basic URL validation
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            return jsonify({'error': 'Please enter a valid URL'}), 400

        # Whitelist of known safe domains
        whitelist = ['google.com', 'www.google.com', 'facebook.com', 'www.facebook.com', 'twitter.com', 'www.twitter.com']

        domain = parsed_url.netloc.lower()

        if domain in whitelist:
            risk_label = "safe"
            confidence_score = 1.0
            features = extract_features(url)
            prediction = 0
        else:
            # Feature extraction
            features = extract_features(url)
            
            # Predict
            prediction = model.predict([features])[0]
            confidence = model.predict_proba([features])[0]

            # Adjust risk labeling using confidence thresholds
            confidence_score = confidence[1]
            risk_label = "safe"
            if confidence_score >= 0.75:
                risk_label = "high-risk"
            elif confidence_score >= 0.4:
                risk_label = "moderate-risk"

        # Log features and prediction for debugging (optional)
        print(f"URL: {url}")
        print(f"Features: {features}")
        print(f"Prediction: {prediction}, Confidence: {confidence_score}")

        return jsonify({
            'url': url,
            'risk': risk_label,
            'confidence': round(confidence_score * 100, 2),
            'features': features
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
