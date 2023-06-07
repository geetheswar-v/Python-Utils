# Python Utils

*Python utils* is project that created by *Group F11*. This project includes data science and as well as some basic application features to learn more about python and it's libraries.

*Our Group Details:*
| Name                    | Roll No. |
|----------|----------|
| Vedachalam Geetheswar   | 142201025   |
| Thota Gunadeep Saran    | 102201027   |
| Devi Shiva Shankar      | 142201028   |
  
  
## ChateMate

**Sequential Model**
___
![seq](https://drive.google.com/uc?export=view&id=12BNFo6hl87VUi5bMDqKiqy2L1S95OaS9)

A **Sequential Model** is a *linear stack of layers* where data flows from one layer to the next, allowing for the transformation and processing of input data. It provides an intuitive and flexible way to construct neural networks for tasks such as classification, regression, and other machine learning applications.
___

**Our Model**
___

Our model is based upon Squential Model where here is simple reference of image of our model:  
![seq_dense](https://drive.google.com/uc?export=view&id=1ujLXc_hNl5IyR7OLm-6cWac-wii59btW)  

**Model Architecture**
- The model is built using TensorFlow's Keras API.
- It uses a sequential model, which means the layers are stacked sequentially.
- The first layer is a dense layer with 256 neurons and a ReLU activation function. It takes the input shape of the training data.
- The dropout layer with a dropout rate of 0.5 helps prevent overfitting by randomly dropping out 50% of the input units during training.
- The second dense layer also has 256 neurons and uses the ReLU activation function.
- Another dropout layer follows, again with a dropout rate of 0.5.
- The final dense layer has a number of neurons equal to the number of tags, and it uses the softmax activation function to output probabilities for tag pattern.
