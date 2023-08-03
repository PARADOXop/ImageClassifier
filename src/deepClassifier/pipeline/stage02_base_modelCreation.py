from deepClassifier import logger
from deepClassifier.components.BaseModel import PrepareBaseModel 
from deepClassifier.config import *
from deepClassifier.constants import *
from deepClassifier.entity import *

Stage_name = 'Base_model_creation'
def main():
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>{Stage_name} started <<<<<<")
        main()
        logger.info(f">>>>>{Stage_name} completed successfully <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e