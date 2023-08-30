# Skin-Cancer-Prediction-using-Deep-Learning
This project is about a simple Skin Cancer Classification model in which User sends the skin cancer image and it classify the skin cancer as benign or malignant. the base training model used here is InceptionV3.Dataset is collected from Kaggle. More information about the algorithm is in the following.

## **Libraries Requirement**

- Numpy
- Tensorflow
- Scikit-Learn
- Matplotlib
- Seaborn
- Keras

## **Dataset collection**

The dataset I used is "Melenoma Skin Cancer Dataset of 10000 images" is available in https://www.kaggle.com/datasets

## **File Description**

- model.ipynb : This file is the base file which trains the CNN model.
- predict.py : This is the flask server file which creates a user interface , retrieve input from user and produce output.
- upload.js : This javascript file is used here to retrieve output from model.
- pred.html/upload.html : These html files are used for web interface.

## **Architecture Insights**

### ImageDataGenerator: 
ImageDataGenerator is used to take the inputs of the original data and then transform it on a random basis, returning theresultant output containing solely the newly changed data. We used this function to reshape, resize, images to grayscale, etc.

### Convulational Neural Network : 
A Convolutional Neural Network (CNN) is a Deep Learning algorithm that can take in an input image, assign importance to various aspects in the image, and be able to differentiate one from the other. We used 4 CNN layers with softmax activation state and 2 fully connected CNN layers.The network is trained with batch size of 128 and epochs of 10.

### SciKit-Learn:
This library is used to acquire accuracy and check train and test differences.

### Matplotlib and Seaborn : 
These libraries were used to visualize the train and test data differences using certain graph models.


