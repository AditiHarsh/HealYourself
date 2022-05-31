from django.apps import AppConfig
import html
import pathlib
import os

#from appointments.model import saved_model
class AppointmentsConfig(AppConfig):
    name = 'appointments'
    '''MODEL_PATH = pathlib.Path("model")
    PRETRAINED_PATH = pathlib.Path("model\saved_model.pb")
    LABEL_PATH = pathlib.Path("label/")
    predictor = saved_model(model_path = MODEL_PATH/"multilabel-emotion-fastbert-basic.bin", 
                                            pretrained_path = PRETRAINED_PATH, 
                                            label_path = LABEL_PATH, multi_label=True)  '''