# === Stage 7: Связи между сущностями ===
# Project: BusRoutes
def get_stops_for_route(route, stops_by_route, integrity_check=True):
    """
    Возвращает список всех «остановка» для заданного «рейс».
    Проверяет целостность связи между рейсом и остановками.
    """
    if not isinstance(route, dict):
        raise TypeError("рейс должен быть словарем")

    route_number = route.get("номер")
    if route_number is None:
        raise ValueError("рейс не содержит поля 'номер'")

    route_id = str(route_number)

    stops = stops_by_route.get(route_id, [])

    if integrity_check:
        for stop in stops:
            if not isinstance(stop, dict):
                raise TypeError("остановка должна быть словарем")
            if "остановка" not in stop:
                raise ValueError("остановка не содержит поля 'остановка'")
            if "рейсы" not in stop:
                raise ValueError("остановка не содержит поля 'рейсы'")

            stop_route_numbers = [str(r.get("номер")) for r in stop.get("рейсы", [])]
            if route_id not in stop_route_numbers:
                raise ValueError(
                    f"остановка '{stop.get('остановка')}' не связана с рейсом {route_id}"
                )

    return stops
