
from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel

STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
            configuration = ConfigurationManager()
            base_model_config = configuration.get_base_model_config()
            base_model = PrepareBaseModel(config=base_model_config)
            base_model.get_base_model()
            base_model.update_base_model()
            
            
if __name__ == "__main__":
    try:
        logger.info(f"stage [{STAGE_NAME}] : Started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"stage [{STAGE_NAME}] : Completed")
    except Exception as e:
        logger.exception(e)
        raise e
       
        
    
    

