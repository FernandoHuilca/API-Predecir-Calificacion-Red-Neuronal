from pydantic import BaseModel
from typing import Optional, List
from pydantic import BaseModel

class TextoEntrada(BaseModel):
    texto: str
    max_tokens: Optional[int] = 100
    temperatura: Optional[float] = 0.7

class StudentData(BaseModel):
    age: int
    study_hours_per_day: float
    social_media_hours: float
    netflix_hours: float
    part_time_job: int
    attendance_percentage: float
    sleep_hours: float
    diet_quality: int
    exercise_frequency: int
    parental_education_level: int
    internet_quality: int
    mental_health_rating: int
    extracurricular_participation: int
    gender_Female: bool
    gender_Male: bool
    gender_Other: bool