from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI #libreria para crear APIs
from app.routes import basic_routes, get_routes, post_routes #Importacion de archivos de rutas
# Crear una instancia de FastAPI
app = FastAPI(
    title="API de Modelo IA - Predecir Calificación",
    description="API para predecir tu futura calificación / rendimiento academico. ",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O pon la URL de tu frontend para más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas
app.include_router(basic_routes.router)
#app.include_router(get_routes.router)
app.include_router(post_routes.router)

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
