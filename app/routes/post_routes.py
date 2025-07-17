# routes/post_routes.py
from fastapi import APIRouter, HTTPException
from app.services.modelo_ia import ModeloIA
from app.models import StudentData

router = APIRouter(tags=["Predicción"])

modelo_ia = ModeloIA() 

@router.post("/predict_grade")
async def predict_grade(data: StudentData):
    try:
        prediccion = modelo_ia.predecir(data.dict())
        return {"predicted_grade": prediccion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

