from flask import Flask, request, jsonify
from detect import analyze_video
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/detect-ai-video', methods=['POST'])
def detect_ai_video():

    print("Incoming request...")
    print("Files received:", request.files)

    if 'video' not in request.files:
        return jsonify({
            "status": "error",
            "message": "No video file found in request"
        }), 400

    video = request.files['video']

    if video.filename == '':
        return jsonify({
            "status": "error",
            "message": "No file selected"
        }), 400

    try:
        video_path = os.path.join(UPLOAD_FOLDER, video.filename)
        video.save(video_path)

        print("Video saved at:", video_path)

        # Correct indentation here
        label, confidence = analyze_video(video_path)

        return jsonify({
            "status": "success",
            "video_status": label,
            "confidence": confidence
        })

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)