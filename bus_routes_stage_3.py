# === Stage 3: Хранилище в памяти ===
# Project: BusRoutes
import random
from collections import defaultdict


class Flight:
    def __init__(self, flight_number, time, capacity, driver):
        self.flight_number = flight_number
        self.time = time
        self.capacity = capacity
        self.driver = driver

    def __repr__(self):
        return (
            f"Flight(flight_number={self.flight_number}, "
            f"time={self.time}, capacity={self.capacity}, driver={self.driver})"
        )


class FlightStore:
    def __init__(self):
        self._flights = {}
        self._counter = 0

    def add_flight(self, flight):
        if flight.flight_number in self._flights:
            raise ValueError(f"Flight {flight.flight_number} already exists")
        self._flights[flight.flight_number] = flight
        return flight

    def get_flight(self, flight_number):
        return self._flights.get(flight_number)

    def list_flights(self):
        return list(self._flights.values())

    def list_flights_on_time(self, time):
        return [flight for flight in self._flights.values() if flight.time == time]

    def count_flights(self):
        return len(self._flights)


def demo():
    store = FlightStore()

    morning = Flight(
        flight_number="M1",
        time="08:00",
        capacity=40,
        driver="Иванов И.И.",
    )
    afternoon = Flight(
        flight_number="A1",
        time="16:30",
        capacity=30,
        driver="Петрова А.С.",
    )

    store.add_flight(morning)
    store.add_flight(afternoon)

    print("Добавлено рейсов:", store.count_flights())

    found = store.get_flight("A1")
    print("Рейс по номеру A1:", found)

    by_time = store.list_flights_on_time("08:00")
    print("Рейсы в 08:00:", by_time)

    all_flights = store.list_flights()
    print("Все рейсы:")
    for flight in all_flights:
        print(" ", flight)


if __name__ == "__main__":
    demo()
