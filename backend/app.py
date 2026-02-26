from flask import Flask, render_template, request, jsonify
from python_url_detector.predict_from_dataset_row import check_url
from model import forensic_audit_web  # your image detection function

app = Flask(__name__)

# -----------------------------
# HOME PAGE
# -----------------------------
@app.route('/')
def index():
    return render_template('index.html')


# -----------------------------
# URL ANALYSIS API
# -----------------------------
@app.route('/analyze-url', methods=['POST'])
def analyze_url():
    try:
        data = request.get_json()

        if not data or 'url' not in data:
            return jsonify({"error": "No URL provided"}), 400

        result = check_url(data['url'])
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# IMAGE ANALYSIS API
# -----------------------------
@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    try:
        if 'image_file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['image_file']

        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        report = forensic_audit_web(file)

        return jsonify(report)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)