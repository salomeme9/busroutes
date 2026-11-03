# === Stage 1: Каркас модуля ===
# Project: BusRoutes
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class Trip:
    number: int
    time: str
    capacity: int
    driver: str


def make_demo_trips() -> List[Trip]:
    """Формирует несколько демонстрационных рейсов."""
    return [
        Trip(number=101, time="07:30", capacity=30, driver="Иванов И.И."),
        Trip(number=102, time="08:00", capacity=40, driver="Петров П.П."),
        Trip(number=103, time="08:30", capacity=25, driver="Сидорова А.С."),
        Trip(number=104, time="09:00", capacity=35, driver="Иванов И.И."),
    ]


def main() -> None:
    trips = make_demo_trips()
    print("Расписание школьного автобуса")
    print("-" * 40)
    for trip in trips:
        print(f"Рейс {trip.number} | {trip.time} | "
              f"мест: {trip.capacity} | водитель: {trip.driver}")
    print("-" * 40)
    print(f"Всего рейсов: {len(trips)}")


if __name__ == "__main__":
    main()
