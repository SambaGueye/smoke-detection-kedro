"""
This is a boilerplate pipeline 'deepL_data_processing'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import processing

# def create_pipeline(**kwargs) -> Pipeline:
#     return pipeline([
#         node(
#             func= processing,
#             inputs=['y_train', 'y_test'],
#             outputs="preprocessed_data_for_DeepL",
#             name="deepL_preprocessing",
#         )
#     ])
