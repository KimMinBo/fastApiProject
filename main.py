from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/toll/{car_type}")
def get_toll(car_type: str):
    toll_fees = {"승용차": 2000, "화물차": 5000, "버스": 3000, "트럭": 4000}
    return {"car_type": car_type, "toll_fee": toll_fees.get(car_type, "요금 정보 없음")}

# 🚀 데이터 구조 정의 (Pydantic 활용)
class CarInfo(BaseModel):
    car_type: str
    owner: str

car_list = []

# ✅ POST 요청 처리
@app.post("/register_car/")
def register_car(car: CarInfo):
    car_list.append(car.dict())  # 차량 정보를 리스트에 추가
    return {
        "message": "차량 등록 완료!",
        "car_type": car.car_type,
        "owner": car.owner
    }

# ✅ GET 요청 처리 (등록된 차량 목록 조회)
@app.get("/cars/")
def get_registered_cars():
    return car_list  # 저장된 차량 리스트 반환