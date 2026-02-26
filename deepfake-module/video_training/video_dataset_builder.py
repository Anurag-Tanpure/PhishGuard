from video_to_frames import extract_frames
import os

def build_dataset(video_folder, label):

    output_path = f"../dataset/{label}"
    os.makedirs(output_path, exist_ok=True)

    for video in os.listdir(video_folder):
        video_path = os.path.join(video_folder, video)

        extract_frames(video_path, output_path)