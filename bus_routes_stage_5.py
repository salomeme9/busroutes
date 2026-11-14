# === Stage 5: Удаление и восстановление ===
# Project: BusRoutes
from datetime import time
from typing import Optional, List


class SoftDeletedFlight:
    def __init__(self, flight_id, number, departure_time, capacity, driver, deleted_at):
        self.flight_id = flight_id
        self.number = number
        self.departure_time = departure_time
        self.capacity = capacity
        self.driver = driver
        self.deleted_at = deleted_at
        self.restored = False

    def restore(self):
        if self.restored:
            return
        self.restored = True

    def to_dict(self):
        return {
            "flight_id": self.flight_id,
            "number": self.number,
            "departure_time": self.departure_time,
            "capacity": self.capacity,
            "driver": self.driver,
            "deleted_at": self.deleted_at,
            "restored": self.restored,
        }


class BusRouteManager:
    def __init__(self):
        self.flights = {}
        self.deleted_flights = {}

    def add_flight(self, number, departure_time, capacity, driver):
        flight_id = f"FLT-{len(self.flights) + 1:04d}"
        self.flights[flight_id] = {
            "number": number,
            "departure_time": departure_time,
            "capacity": capacity,
            "driver": driver,
        }
        return flight_id

    def get_flight(self, flight_id):
        return self.flights.get(flight_id)

    def delete_flight(self, flight_id):
        if flight_id not in self.flights:
            return False
        flight = self.flights.pop(flight_id)
        self.deleted_flights[flight_id] = SoftDeletedFlight(
            flight_id,
            flight["number"],
            flight["departure_time"],
            flight["capacity"],
            flight["driver"],
            time(0, 0),
        )
        return True

    def restore_flight(self, flight_id):
        soft = self.deleted_flights.get(flight_id)
        if soft is None or soft.restored:
            return False
        self.flights[flight_id] = {
            "number": soft.number,
            "departure_time": soft.departure_time,
            "capacity": soft.capacity,
            "driver": soft.driver,
        }
        del self.deleted_flights[flight_id]
        return True

    def list_deleted_flights(self):
        return [f.to_dict() for f in self.deleted_flights.values()]

    def list_restorable_flights(self):
        return [f.to_dict() for f in self.deleted_flights.values() if not f.restored]
