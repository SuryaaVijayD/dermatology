from flask import Flask, request, render_template ,jsonify, make_response
import os
import cv2
from keras.models import load_model  
from PIL import Image, ImageOps  
import numpy as np

app = Flask(__name__)

# Define the upload directory
UPLOAD_FOLDER = r'C:\Users\Admin\Documents\dermatalogy\python_folder\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


image_files = [os.path.join(UPLOAD_FOLDER, filename) for filename in os.listdir(UPLOAD_FOLDER) if filename.endswith(('.jpg', '.png'))]

@app.route('/')
def index():
    return render_template('darmahtml.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'imageFile' not in request.files:
        return "No file part"

    file = request.files['imageFile']

    if file.filename == '':
        return "No selected file"

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        print(file)

        final = image_processing(file)

        return render_template('result.html', result=final)
    

def image_processing(image_files):
    results = []  

    image = Image.open(image_files)
    np.set_printoptions(suppress=True)
    model = load_model(r"C:\Users\Admin\Documents\model list\keras_model.h5", compile=False)
    class_names = open(r"C:\Users\Admin\Documents\model list\labels.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image_process = image.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image_process, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array
    
    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    
    result = "Class: " + str(class_name[2:])
    
    results.append(result)  # Add the result to the list

    print("Confidence Score:", confidence_score)
    return results



if __name__ == '__main__':
    app.run(debug=True)
