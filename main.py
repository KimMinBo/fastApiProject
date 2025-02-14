from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/toll/{car_type}")
def get_toll(car_type: str):
    toll_fees = {"승용차": 2000, "화물차": 5000, "버스": 3000}
    return {"car_type": car_type, "toll_fee": toll_fees.get(car_type, "요금 정보 없음")}