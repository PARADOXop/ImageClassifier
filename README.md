# deep Classifier project

## workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline

![img](https://dagshub.com/PARADOXop/DEEPCNNClassifier/src/master/docs/images/Data%20Ingestion@2x%20%281%29.png)


STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/PARADOXop/DEEPCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=PARADOXop \
MLFLOW_TRACKING_PASSWORD=<> \

STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model


## Sample data for testing-
https://raw.githubusercontent.com/c17hawke/raw_data/main/sample_data.zip



mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./artifacts \
--host 0.0.0.0 -p 1234

conda activate C:/Users/rkuka/miniconda3 \
conda activate P:/DEEPCNNClassifier/env