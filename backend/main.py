from fastapi import FastAPI

app = FastAPI(title="Smart Maintenance QR API")

@app.get("/")
def read_root():
    return {"mensaje": "API de Smart Maintenance QR funcionando correctamente"}