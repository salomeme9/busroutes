# === Stage 9: Фильтрация записей ===
# Project: BusRoutes
def filter_trips_by_time(trips, time_value):
    """Фильтрует рейсы по точному значению поля 'время'."""
    return [trip for trip in trips if trip["time"] == time_value]


def filter_trips_by_date_range(trips, start_date, end_date):
    """Фильтрует рейсы по диапазону дат.

    start_date и end_date — строки в формате 'YYYY-MM-DD'.
    Рейсы, чья дата совпадает с начальной или конечной датой диапазона,
    включаются в результат.
    """
    filtered = []
    for trip in trips:
        trip_date = trip.get("date")
        if trip_date:
            if start_date <= trip_date <= end_date:
                filtered.append(trip)
    return filtered


def filter_trips(trips, time_value=None, start_date=None, end_date=None):
    """Функция-обёртка для комбинированной фильтрации рейсов.

    Можно указать любое подмножество критериев:
    - time_value: точное совпадение значения поля 'время'.
    - start_date, end_date: диапазон дат в формате 'YYYY-MM-DD'.
    Критерии объединяются логически (И).
    """
    if time_value is not None and start_date is not None and end_date is not None:
        trips = filter_trips_by_time(trips, time_value)
        trips = filter_trips_by_date_range(trips, start_date, end_date)
    elif time_value is not None:
        trips = filter_trips_by_time(trips, time_value)
    elif start_date is not None and end_date is not None:
        trips = filter_trips_by_date_range(trips, start_date, end_date)
    return trips


if __name__ == "__main__":
    sample_trips = [
        {"number": 1, "time": "07:30", "capacity": 30, "driver": "Иванов", "date": "2024-01-15"},
        {"number": 2, "time": "08:00", "capacity": 25, "driver": "Петров", "date": "2024-01-16"},
        {"number": 3, "time": "07:30", "capacity": 40, "driver": "Сидоров", "date": "2024-01-17"},
        {"number": 4, "time": "09:15", "capacity": 20, "driver": "Козлов", "date": "2024-01-18"},
    ]

    print("Фильтрация по времени '07:30':")
    for trip in filter_trips_by_time(sample_trips, "07:30"):
        print(f"  Рейс {trip['number']}, водитель {trip['driver']}, дата {trip['date']}")

    print("Фильтрация по диапазону дат '2024-01-15' до '2024-01-17':")
    for trip in filter_trips_by_date_range(sample_trips, "2024-01-15", "2024-01-17"):
        print(f"  Рейс {trip['number']}, время {trip['time']}, водитель {trip['driver']}")

    print("Комбинированная фильтрация (время '07:30' и дата '2024-01-15'..'2024-01-17'):")
    for trip in filter_trips(sample_trips, "07:30", "2024-01-15", "2024-01-17"):
        print(f"  Рейс {trip['number']}, водитель {trip['driver']}, дата {trip['date']}")
