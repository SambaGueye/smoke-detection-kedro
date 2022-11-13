"""
This is a boilerplate pipeline 'general_data_processing'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import general_processing

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=general_processing,
            inputs="smoke_detection_dataset",
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="general_preprocessing",
        )
    ])
