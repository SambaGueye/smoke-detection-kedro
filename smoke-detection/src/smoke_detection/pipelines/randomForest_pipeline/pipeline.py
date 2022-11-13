"""
This is a boilerplate pipeline 'randomForest_pipeline'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_RF_model, RF_evaluation

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_RF_model,
            inputs=["X_train", "y_train"],
            outputs="clf",
            name="RF_model",
        ),
        node(
            func=RF_evaluation,
            inputs=["clf","X_test", "y_test"],
            outputs="rfc_metrics",
            name="RF_model_evaluation",
        )
    ])
