import json
import logging
from src.pipeline import BERTPuncResto
from src.preprocess_func import create_movies_dataset
#from src.multigpu_pipeline import PunctuationRestorationPipeline

logging.basicConfig(level=logging.INFO)


def main(config_file="config/train.json"):

    with open(config_file) as f:
        config = json.load(f)
    logging.info("Config : %s" % config)

    model = BERTPuncResto(**config["general"], **config["data"])
    model.train_model(**config["training"])


if __name__ == "__main__":
    main()

