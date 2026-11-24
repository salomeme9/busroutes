# === Stage 10: Сортировка записей ===
# Project: BusRoutes
from datetime import datetime


def sort_bus_rides(rides, by_number=False, by_created=False, reverse=False):
    """
    Сортирует список записей «рейс» (словарей) по номеру рейса и/или
    дате создания.

    Параметры:
        rides      - список словарей с полями номер и created.
        by_number  - если True, сортировка по полю «номер».
        by_created - если True, сортировка по полю «created» (datetime).
        reverse    - если True, сортировка в порядке убывания.

    Возвращает новый отсортированный список (исходный не изменяется).
    """
    def sort_key(ride):
        key = []
        if by_number:
            key.append(ride.get("number"))
        if by_created:
            key.append(ride.get("created"))
        return tuple(key)

    return sorted(rides, key=sort_key, reverse=reverse)


def main():
    sample_rides = [
        {
            "number": "B-102",
            "time": "08:15",
            "capacity": 30,
            "driver": "Иванов",
            "created": datetime(2024, 1, 3, 10, 0),
        },
        {
            "number": "B-101",
            "time": "08:05",
            "capacity": 25,
            "driver": "Петров",
            "created": datetime(2024, 1, 5, 9, 30),
        },
        {
            "number": "B-103",
            "time": "08:30",
            "capacity": 20,
            "driver": "Сидоров",
            "created": datetime(2024, 1, 1, 8, 0),
        },
        {
            "number": "B-104",
            "time": "08:45",
            "capacity": 35,
            "driver": "Козлов",
            "created": datetime(2024, 1, 2, 11, 15),
        },
    ]

    by_created_asc = sort_bus_rides(
        sample_rides, by_created=True, reverse=False
    )
    by_number_desc = sort_bus_rides(
        sample_rides, by_number=True, reverse=True
    )
    by_both_asc = sort_bus_rides(
        sample_rides, by_number=True, by_created=True, reverse=False
    )

    for ride in by_created_asc:
        print("По дате создания (возр.):", ride["number"], ride["created"])
    print()
    for ride in by_number_desc:
        print("По номеру (убыв.):", ride["number"], ride["created"])
    print()
    for ride in by_both_asc:
        print("По номеру и дате (возр.):", ride["number"], ride["created"])


if __name__ == "__main__":
    main()
