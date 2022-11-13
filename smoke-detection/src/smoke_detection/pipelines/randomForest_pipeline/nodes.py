"""
This is a boilerplate pipeline 'randomForest_pipeline'
generated using Kedro 0.18.3
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
import logging


def train_RF_model(X_train, y_train):
    clf = RandomForestClassifier(max_depth=2, random_state=10)
    clf.fit(X_train, y_train)
    return clf


def RF_evaluation(clf:RandomForestClassifier, X_test, y_test):
    y_pred = clf.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    f_score = f1_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a accuracy of %.3f on test data.", score)
    logger.info("Model has a f1 score of %.3f on test data.", f_score)
    logger.info("Model has a recall of %.3f on test data.", recall)
    
    return {"accuracy": score,
            "f1_score" : f_score,
            "recall" : recall}