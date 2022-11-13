"""
This is a boilerplate pipeline 'deepL_data_processing'
generated using Kedro 0.18.3
"""
from keras.utils import to_categorical

def processing(y_train, y_test):
    # Applying the function to training set labels and testing set labels
    
    y_train = to_categorical(y_train, dtype ="uint8")
    y_test = to_categorical(y_test, dtype ="uint8")

    return y_train, y_test