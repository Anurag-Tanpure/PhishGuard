import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("deepfake_model.h5")

THRESHOLD = 0.65

def predict_frame(frame):

    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0
    frame = np.reshape(frame, (1, 224, 224, 3))

    prediction = model.predict(frame)[0][0]

    confidence = float(prediction)

    if prediction > THRESHOLD:
        return "Fake", confidence
    else:
        return "Real", 1 - confidence