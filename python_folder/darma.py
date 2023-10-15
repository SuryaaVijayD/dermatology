from flask import Flask, request, render_template ,jsonify, make_response
import os
import cv2
import pandas as pd
from keras.models import load_model  
from PIL import Image, ImageOps  
import numpy as np

app = Flask(__name__)



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

        return render_template('result.html', result=final[0])
    

def image_processing(image_files):
    results = []  

    image = Image.open(image_files)
    np.set_printoptions(suppress=True)
    model = load_model(r"C:\Users\Admin\Downloads\skin_model.h5", compile=False)
    class_names = open(r"C:\Users\Admin\Downloads\skin_label.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image_process = image.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image_process, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array
    
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    
    result = "Class: " + str(class_name[2:])
    
    results.append(result)  

    print("Confidence Score:", confidence_score)
    return results

@app.route('/hair', methods=['POST'])
def hair():
    if 'imageFile' not in request.files:
        return "No file part"

    file = request.files['imageFile']

    if file.filename == '':
        return "No selected file"

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        final = hair_image_processing(file)

        return render_template('result.html', result=final[0])

def hair_image_processing(file):
    results = []
    image = Image.open(image_files)
    np.set_printoptions(suppress=True)

    model = load_model(r"C:\Users\Admin\Downloads\hair_model.h5", compile=False)

    class_names = open(r"C:\Users\Admin\Downloads\hair_label.txt", "r").readlines()

    '''['0 acne keloidalis\n', '1 alopecia areata\n', '2 trichotillomania\n']'''

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = image.convert("RGB")
    #image = Image.open(r"captured_image.jpg").convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    
    print("Confidence Score:", confidence_score)
    return class_name


    

dermatologists_data = pd.read_csv(r'C:\Users\Admin\Downloads\doctordata.csv')
@app.route('/doc_recommendation', methods=['POST'])
def doc_recommendation():
    
    user_skin_disease = request.form['skin_disease']
    user_location = request.form['location']
    print(user_skin_disease,user_location)

    dermatologists_with_skin_disease = dermatologists_data[dermatologists_data['Specialization'] == user_skin_disease]

    dermatologists_in_user_location = dermatologists_with_skin_disease[dermatologists_with_skin_disease['Location'] == user_location]

    recommended_dermatologists = dermatologists_in_user_location.sort_values(by='Patient_Rating', ascending=False).head(5)

    return render_template('docRecommend.html', recommendations=recommended_dermatologists.to_html(classes='table table-striped'))



if __name__ == '__main__':
    app.run(debug=True)