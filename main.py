from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "美团外卖API"}
@app.get("/shops")
def shops(lat: float = 39.9, lng: float = 116.4):
    return {"success": True, "shops": [{"name": "店铺1", "rating": 4.5}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
