import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("deepfake_model.h5")

def predict_frame(frame):

    frame = cv2.resize(frame, (224,224))
    frame = frame / 255.0
    frame = np.reshape(frame, (1,224,224,3))

    prediction = model.predict(frame)

    if prediction > 0.5:
        return "Fake"
    else:
        return "Real"