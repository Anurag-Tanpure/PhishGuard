import cv2
from predict import predict_frame

def analyze_video(video_path):

    cap = cv2.VideoCapture(video_path)

    fake_scores = []
    real_scores = []

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 5 == 0:
            label, confidence = predict_frame(frame)

            if label == "Fake":
                fake_scores.append(confidence)
            else:
                real_scores.append(confidence)

        frame_count += 1

    cap.release()

    avg_fake = sum(fake_scores)/len(fake_scores) if fake_scores else 0
    avg_real = sum(real_scores)/len(real_scores) if real_scores else 0

    fake_count = len(fake_scores)
    real_count = len(real_scores)

    total = fake_count + real_count

    if total == 0:
        return "Uncertain", 0.0, "No frames analyzed"

    fake_ratio = fake_count / total
    real_ratio = real_count / total

    if fake_ratio > 0.75:
        return "Fake", round(avg_fake,2), "Frame texture inconsistency detected"

    elif real_ratio > 0.55:
        return "Real", round(avg_real,2), "Natural facial consistency observed"

    else:
        return "Uncertain", round(max(avg_fake, avg_real),2), "Mixed frame signals detected"