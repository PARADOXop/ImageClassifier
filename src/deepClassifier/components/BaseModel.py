from deepClassifier.constants import *
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier.entity import PrepareBaseModelConfig
import os
import urllib.request as request
from zipfile import ZipFile
from deepClassifier import logger
from deepClassifier.utils.common import get_size
from tqdm import tqdm
import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        logger.info("Preparing base model")
        self.model = tf.keras.applications.vgg16.VGG16(
            weights=self.config.params_weights,
            include_top=self.config.params_include_top,
            input_shape=self.config.params_image_size
        )
        
        logger.info("prepared base model")
        self.save_model(path = self.config.base_model_path, model= self.model)
        logger.info(f"Base model saved at {self.config.base_model_path}")
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        logger.info(f"Preparing full model with classes: {classes}, freeze_all: {freeze_all}, freeze_till: {freeze_till}, learning_rate: {learning_rate}")  
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif freeze_till and freeze_till >0:
            for layer in model.layers[:freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
                        activation='softmax'
        )(flatten_in)
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )
        logger.info("Model output is prepared for training")
        full_model.compile(
                    optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                    loss='categorical_crossentropy',
                    metrics=['accuracy']
                )
        logger.info("Model is compiled successfully using the following training parameters optimizer ")
        return full_model
    def update_base_model(self):
        logger.info("Updating base model")
        self.full_model = self._prepare_full_model(
        model = self.model, 
        classes = self.config.params_classes,
        freeze_all = True,
        freeze_till = 15,
        learning_rate = self.config.params_learning_rate
    
        )
        self.save_model(path= self.config.updated_base_model_path, model = self.full_model)
        logger.info(f"saved the updated model at {self.config.updated_base_model_path}")
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
    