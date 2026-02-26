from model import build_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = build_model()

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train = datagen.flow_from_directory(
    "../dataset",
    target_size=(224,224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val = datagen.flow_from_directory(
    "../dataset",
    target_size=(224,224),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

model.fit(train, validation_data=val, epochs=5)

model.save("../deepfake_model.h5")