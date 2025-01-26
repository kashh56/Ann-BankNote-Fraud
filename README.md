Bank Note Fraud Prediction
==========================

**Bank Note Fraud Prediction** is a machine learning project aimed at predicting whether a banknote is real or fake based on certain features such as variance, skewness, curtosis, and entropy. The project uses a  Artificial Neural Network and has been tuned for optimal performance. The model has been deployed via Streamlit to allow users to predict fraudulence in real-time by entering banknote characteristics.

Table of Contents
-----------------

*   [About](#about)
*   [Dataset](#dataset)
*   [Model](#model)
*   [Hyperparameter Tuning](#hyperparameter-tuning)
*   [Streamlit Deployment](#streamlit-deployment)
*   [Contributing](#contributing)
*   [License](#license)

About
-----

The goal of this project is to build a machine learning model that can predict whether a given banknote is real or counterfeit based on a set of features. The features include:

*   Variance of the wavelet transformed image
*   Skewness of the wavelet transformed image
*   Curtosis of the wavelet transformed image
*   Entropy of the image

The model predicts a binary output: **0** for real notes and **1** for counterfeit notes.

Dataset
-------

The dataset used for this project is the \*\*Banknote Authentication dataset\*\*. It consists of 1372 samples, with 4 numerical features and a target variable. The features in the dataset are:

*   Variance (continuous)
*   Skewness (continuous)
*   Curtosis (continuous)
*   Entropy (continuous)

The target variable is a binary classification label: **0** for genuine notes and **1** for fraudulent notes.

Model
-----

The machine learning model used for predicting banknote fraud :
*   Artificial Neural Network (ANN)



Hyperparameter Tuning
---------------------

Hyperparameter tuning was performed to improve model performance using Keras Tuner :

*   Number of nodes
*   Activation function
*   Number of hidden layers


Streamlit Deployment
--------------------

Once the model was trained and optimized, it was deployed using **Streamlit** to make the prediction process more interactive and user-friendly. With Streamlit, users can input the features of a banknote and get a prediction on whether the note is fraudulent or not.

To interact with the model on Streamlit, visit the deployed app:

[Live Streamlit App](https://ann-banknote-fraud-akash.streamlit.app/)


Contributing
------------

If you would like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Please ensure the following guidelines are followed:

*   Follow the existing coding style
*   Write unit tests for new features or changes
*   Update the documentation as needed

License
-------

This project is licensed under the MIT License -
