# Skin-Cancer-Prediction-using-Deep-Learning
This project is about a simple Skin Cancer Classification model in which User sends the skin cancer image and it classify the skin cancer as benign or malignant. the base training model used here is CNN. More information about the algorithm is in the following.

## **Libraries Requirement**

- Numpy
- Tensorflow
- Scikit-Learn
- Matplotlib
- Seaborn
- Keras

## **File Description**

- model.ipynb : This file is the base file which trains the CNN model.


## **Architecture Insights**

### ImageDataGenerator: 
ImageDataGenerator is used to take the inputs of the original data and then transform it on a random basis, returning the output resultant containing solely the newly changed data. We used this function to reshape, resize, images to grayscale, etc.

### Convulational Neural Network : 
A Convolutional Neural Network (CNN) is a Deep Learning algorithm that can take in an input image, assign importance to various aspects in the image, and be able to differentiate one from the other. We used 4 CNN layers with softmax activation state and 2 fully connected CNN layers.The network is trained with batch size of 128 and epochs of 10.

### Matplotlib and Seaborn : 
These libraries were used to visualize the train and test data differences using certain graph models.

### SciKit-Learn:
This library is used to acquire accuracy and check train and test differences.
