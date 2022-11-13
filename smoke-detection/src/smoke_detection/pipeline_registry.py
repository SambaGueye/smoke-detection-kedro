"""Project pipelines."""
from typing import Dict
from smoke_detection.pipelines import general_data_processing as ds
from smoke_detection.pipelines import randomForest_pipeline as rf
from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # pipelines = find_pipelines()
    # pipelines["__default__"] = sum(pipelines.values())
    # return pipelines
    
    data_processing_pipeline = ds.create_pipeline()
    data_science_pipeline = rf.create_pipeline()

    return {
        "__default__": data_processing_pipeline + data_science_pipeline,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
    }