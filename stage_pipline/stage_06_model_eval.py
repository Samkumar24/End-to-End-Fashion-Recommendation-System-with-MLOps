from src.recommendation_system.config.config import Config_manager
from src.recommendation_system.components._06_model_evaluation import model_evalulation_config



class model_eval_pipline:

    def __init__(self):
        pass

    def main(self):


        con= Config_manager()              # ← create config manager
        model_config = con.get_model_evaluation()   # ← get model eval config
        model  = model_evalulation_config(model_config)  # ← pass config
        model.run_evaluation()        

