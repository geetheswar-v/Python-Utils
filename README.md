# Python Utils

**Python utils** is project that created by **Group F11**. This project includes data science and as well as some basic application features to learn more about python and it's libraries.

**Our Group Details:**
| Name                    | Roll No. |
|----------|----------|
| Vedachalam Geetheswar   | 142201025   |
| Thota Gunadeep Saran    | 102201027   |
| Devi Shiva Shankar      | 142201028   |
  
  
## 1. ChatMate

  A Chatbot that can give information of Our Insitiute Details. Since we have less knowledge about Deep Learning we tried our best to make some improvements in our project like adding live data getting weather details using Open Weather API, e.t.c.  
  ![seq](https://drive.google.com/uc?export=view&id=1eHX1FlEsd9OQSzOCFOP9-k0vXQl996Gp)

  ### Sequential Model
  ___
  ![seq](https://drive.google.com/uc?export=view&id=12BNFo6hl87VUi5bMDqKiqy2L1S95OaS9)

  A **Sequential Model** is a *linear stack of layers* where data flows from one layer to the next, allowing for the transformation and processing of input data. It provides an intuitive and flexible way to construct neural networks for tasks such as classification, regression, and other machine learning applications.

  ### Our Model
  ___

  Our model is based upon Squential Model where here is simple reference of image of our model:  
  ![seq_dense](https://drive.google.com/uc?export=view&id=1ujLXc_hNl5IyR7OLm-6cWac-wii59btW)  

  ### Data Preprocessing:
  - The data has patteren and responses with respect to tags
  - The patterns are tokenized using NLTK's tokenizer, which splits them into individual words.
  - The lemmatizer is used to transform the words into their base form.
  - Tags converted into encoded vectors, where each vector has a value of 1 for the corresponding tag and 0 for others.
  - It combines the bag-of-words representation with the encoded vectors to create the training dataset.

  ### Model Architecture
  - The model is built using TensorFlow's Keras API.
  - It uses a sequential model, which means the layers are stacked sequentially.
  - The first layer is a dense layer with 256 neurons and a ReLU activation function. It takes the input shape of the training data.
  - The dropout layer with a dropout rate of 0.5 helps prevent overfitting by randomly dropping out 50% of the input units during training.
  - The second dense layer also has 256 neurons and uses the ReLU activation function.
  - Another dropout layer follows, again with a dropout rate of 0.5.
  - The final dense layer has a number of neurons equal to the number of tag.
  - The final dense uses the softmax activation function to output probabilities for tag pattern.
  - Categorical cross-entropy loss is used because it is suitable for multi-class classification problems.
  - The Adam optimizer is used with a learning rate of 0.0001, which adjusts the model's weights during training.

## 2. Stock Prediction App

A simple stock predictor app using **Facebook Prophet**. It is a forecasting tool developed by Facebook's Data Science team. It is designed to make time series forecasting accessible and easy to use, even for users without a deep background in statistics. Prophet incorporates several advanced features, such as seasonality modeling and trend flexibility, to provide accurate and reliable forecasts for a wide range of applications.
![stock1](https://drive.google.com/uc?export=view&id=15b0gcmI7-3jFFficxAn3QQeBKXcPCrHj)
![stock2](https://drive.google.com/uc?export=view&id=1Dcijo-d_Yl0L4ciqZcTslq-cHy1rYZsz)

## 3. Calculator App
A Simple Calculator and Conveter Application which is inbuilt from scratch using Datastructures and stacks for procedence.

**Code Structure:**  

    evaluator/tokens.py       # Helper class to tokenize
    evaluator/parser.py       # Helper class to parse the expersion to postfix
    evaluator/evaluator.py    # Helper class to evaluate the postfix expersion
    conveter.py               # Helper class to convert any units    
    
    
![stock1](https://drive.google.com/uc?export=view&id=1vclYos_iVcaFrlSlyPRpu-3aoxR_FLES)

## 4. Weather App
A Simple Weather App using Open Weather Api to fetch details of weather of a specific city by poviding the name.

___

## Modules Used:
1. ChatMate
    - Tensorflow
    - NLTK
    - Numpy
    - Json
    - Pickle
    - re
2. Stocks
    - Yfinance
    - Prophet
3. Weather
     - Requests
     - Json
