# **Dermatology Skin Care Prediction Web and Mobile Application**
This project aims to provide users with a convenient platform to predict skin and hair-related issues using image classification techniques. 
The application consists of both web and mobile versions, allowing users to access it from different devices. Below is an overview of the project structure, functionalities, and usage instructions.

## **Features:**
Skin and Hair Issue Prediction: Users can upload images of their skin or hair to the application, which will then analyze the image to predict any related issues.
 ### **Disease Awareness:** 
 For detected issues, the application provides information and awareness about the disease, including its symptoms, causes, and preventive measures.
 ### **Doctor Recommendation:** 
 In case of severe conditions, the application recommends nearby dermatologists for consultation.
### **Responsive Design:** 
Both web and mobile versions of the application are designed to be responsive, providing a seamless user experience across different devices.

## **Project Structure:**
## **Web Version:**
dermahtml.html: Main HTML file containing project description and navigation functionality.
indexCss.css: CSS file for styling the web interface.
derma.py: Flask application responsible for handling image uploads, processing, and disease prediction.
### **Usage:**
 **Web Version:**
Navigate to dermahtml.html to access the main page of the web application.
Click on the "Get Started" button to proceed.
Choose between skin-related or hair-related issues to proceed with classification.
Upload an image of the affected area for analysis.
Receive predictions and disease awareness information based on the uploaded image.
For severe conditions, consult nearby dermatologists as recommended by the application.
### **Dependencies:**
1.Flask
2.OpenCV
3.Keras
4.Pandas
5.NumPy
6.PIL (Python Imaging Library)

## **Running the Application:**
Clone this repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run the Flask application by executing python derma.py.
Access the web application through your preferred web browser.

## **Disclaimer:**
This application provides information and predictions based on image analysis and machine learning models. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any medical concerns or conditions.

