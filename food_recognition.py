from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
class_labels = ['freshapples', 'freshbanana', 'freshoranges', 'rottenapples', 'rottenbanana', 'rottenoranges']
model = load_model('food_classification_model.h5')
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def predict_class(image_path):
    # Preprocess the image
    img = preprocess_image(image_path)

    # Predict class probabilities
    predictions = model.predict(img)
    
    # Get predicted class label
    predicted_class = class_labels[np.argmax(predictions)]

    return predicted_class