import numpy as np
from tensorflow.keras.models import load_model
import joblib

class ModeloIA:
    def __init__(self):
        # Cargar el modelo y el scaler entrenados
        self.model = load_model('app/services/modelo_ann.h5', compile=False)
        self.scaler = joblib.load('app/services/scaler.pkl')

    def predecir(self, data_dict):
        input_data = np.array([[
            data_dict['age'],
            data_dict['study_hours_per_day'],
            data_dict['social_media_hours'],
            data_dict['netflix_hours'],
            data_dict['part_time_job'],
            data_dict['attendance_percentage'],
            data_dict['sleep_hours'],
            data_dict['diet_quality'],
            data_dict['exercise_frequency'],
            data_dict['parental_education_level'],
            data_dict['internet_quality'],
            data_dict['mental_health_rating'],
            data_dict['extracurricular_participation'],
            int(data_dict['gender_Female']),
            int(data_dict['gender_Male']),
            int(data_dict['gender_Other'])
        ]])
        # Normalizar igual que en el entrenamiento
        input_scaled = self.scaler.transform(input_data)
        # Predicir
        pred = self.model.predict(input_scaled)
        return float(pred[0][0])