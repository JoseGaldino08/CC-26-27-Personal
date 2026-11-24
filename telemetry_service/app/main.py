from fastapi import FastAPI

#Beta 
app = FastAPI(
    title="AgroSense Telemetry Service",
    description="Receives and manages agricultural sensor data",
    version="0.1.0"
)

#Não conectado a SQL ainda
telemetry_records = []

@app.get("/health")
def health():
    return {"status": "healthy"}

