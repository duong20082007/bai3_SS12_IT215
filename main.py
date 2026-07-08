from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base
from schemas import ShipmentUpdate, ShipmentResponse
from shipment_services import update_shipment_service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Shipment Update API")

@app.put(
    "/shipments/{shipment_id}", 
    response_model=ShipmentResponse, 
    status_code=status.HTTP_200_OK
)
def update_shipment(
    shipment_id: int, 
    shipment_update: ShipmentUpdate, 
    db: Session = Depends(get_db)
):
    updated_shipment = update_shipment_service(
        db=db, 
        shipment_id=shipment_id, 
        shipment_update=shipment_update
    )
    
    return updated_shipment