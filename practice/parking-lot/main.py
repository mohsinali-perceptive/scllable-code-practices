"""
- parking lot contains many parking spots of type Car, Truck, Bike
- Each vehicle is assigned parking ticket on entry
- Parking fee based on total time and vehicle type
- support multiple payment
- successfull payment -> free the slot



Key componenents:
class VehicleType(Enum):
    Truck, Car, Bike

class ParkingSpot:
    id : int
    type: VehicleType
    is_occupied: boolean

class ParkingTicket:
    ticket_id: int
    vehicle: Vehicle
    in_time: datetime
    out_time: datetime
    spot: ParkingSpot
    amount: int
    is_payment_complete: boolean

class Vehicle:
    type: VehicleType
    licence_plate: str


class ParkingLot:
    ParkingSpot[]

class PaymentTypes:
    UPI, credit_card, debit_card

class PaymentStrategy:
    def process_payment(amount: int)

class ParkingSpotManager:


"""


