import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
import shutil
import os
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.common import read_yaml, create_directories,save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)  # ✅ FIXED HERE
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    
    
    def log_into_mlflow(self):
        
        
        mlflow.set_tracking_uri("https://dagshub.com/Nisargak18/Kidney-Disease-Classification-Deep-Learning-Project.mlflow")
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        mlflow.set_experiment("default")

        with mlflow.start_run():
             mlflow.log_param("test_param", 1)
             mlflow.log_metric("test_metric", 0.99)
            # Save model to a temp dir
             model_dir = "temp_model_dir"
             model_path = os.path.join(model_dir, "model.h5")
             os.makedirs(model_dir, exist_ok=True)
             self.model.save(model_path)

            # Log model as artifact (not as registered model)
             mlflow.log_artifact(model_path, artifact_path="VGG16Model")

            # Clean up
             shutil.rmtree(model_dir)