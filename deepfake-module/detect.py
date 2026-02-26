import cv2
from predict import predict_frame

def analyze_video(video_path):

    cap = cv2.VideoCapture(video_path)

    fake_count = 0
    real_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = predict_frame(frame)

        if result == "Fake":
            fake_count += 1
        else:
            real_count += 1

    cap.release()

    if fake_count > real_count:
        return "Fake Video"
    else:
        return "Real Video"