import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from PIL import Image
import io
import os

app = Flask(__name__)

# Charger le modèle TensorFlow Lite
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Obtenir les détails des tensors (entrées et sorties)
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Dictionnaire des classes, l'index correspond à l'index prédit
class_names = {
    0: 'Pepper__bell___Bacterial_spot',
    1: 'Pepper_bell_healthy',
    2: 'Potato_Early_blight',
    3: 'Potato_Late_blight',
    4: 'Potato_healthy',
    5: 'Tomato_Bacterial_spot',
    6: 'Tomato_Early_blight',
    7: 'Tomato_Late_blight',
    8: 'Tomato_Leaf_Mold',
    9: 'Tomato_Septoria_leaf_spot',
    10: 'Tomato_Spider_mites_Two_spotted_spider_mite',
    11: 'Tomato_Target_Spot',
    12: 'Tomato__Tomato_YellowLeaf__Curl_Virus',
    13: 'Tomato__Tomato_mosaic_virus',
    14: 'Tomato_healthy',
    15: 'Classe_inconnue'  # Assurez-vous que cette classe est correctement définie dans votre modèle
}

# Prétraiter l'image pour l'adapter au modèle
def preprocess_image(image):
    image = image.resize((224, 224))  # Taille d'entrée du modèle
    image = np.array(image)
    image = np.expand_dims(image, axis=0).astype(np.float32)  # Ajouter la dimension batch
    image = image / 255.0  # Normalisation
    return image

# Fonction pour prédire la classe
def predict_image(image):
    input_data = preprocess_image(image)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Charger l'image
    image = Image.open(file.stream)

    # Prédiction
    prediction = predict_image(image)
    predicted_index = np.argmax(prediction, axis=1)[0]

    # Vérifier si l'index est dans la plage valide
    if predicted_index >= len(class_names):
        predicted_class_name = 'Classe inconnue'
    else:
        predicted_class_name = class_names.get(predicted_index, 'Classe inconnue')

    # Retourner le nom de la classe prédite
    return jsonify({'predicted_class': predicted_class_name})

if __name__ == '__main__':
    app.run(debug=True)
