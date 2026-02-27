from video_dataset_builder import build_dataset

print("Extracting REAL videos...")
build_dataset("../video_data/real", "real")

print("Extracting FAKE videos...")
build_dataset("../video_data/fake", "fake")

print("Dataset built from videos!")