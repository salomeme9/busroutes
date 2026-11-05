# === Stage 2: Проверка полей ===
# Project: BusRoutes
import datetime


class BusRouteValidationError(Exception):
    def __init__(self, route_number, message):
        self.route_number = route_number
        self.message = message
        super().__init__(f"Рейс {route_number}: {message}")


def normalize_route_number(value):
    value = value.strip()
    if not value:
        return None
    cleaned = "".join(ch for ch in value if ch.isdigit())
    if not cleaned:
        return None
    return cleaned.zfill(4)


def normalize_time(value):
    value = value.strip()
    if not value:
        return None
    try:
        return datetime.time.fromisoformat(value.split()[0])
    except ValueError:
        return None


def normalize_capacity(value):
    value = value.strip()
    if not value:
        return None
    try:
        capacity = int(value)
    except ValueError:
        return None
    if capacity <= 0:
        return None
    return capacity


def normalize_driver(value):
    value = value.strip()
    if not value:
        return None
    if len(value) < 2:
        return None
    return value


def validate_route(route_number, time, capacity, driver):
    if route_number is None:
        raise BusRouteValidationError(None, "Номер рейса обязателен.")
    if not route_number.isdigit():
        raise BusRouteValidationError(route_number, "Номер рейса должен состоять только из цифр.")

    if time is None:
        raise BusRouteValidationError(route_number, "Время отправления обязательное.")
    if not (0 <= time.hour < 24 and 0 <= time.minute < 60):
        raise BusRouteValidationError(route_number, "Время должно быть в формате ЧЧ:ММ.")

    if capacity is None:
        raise BusRouteValidationError(route_number, "Вместимость должна быть положительным числом.")

    if driver is None:
        raise BusRouteValidationError(route_number, "Водитель обязателен.")
    if len(driver) < 2:
        raise BusRouteValidationError(route_number, "Имя водителя должно содержать минимум две буквы.")

    return route_number, time, capacity, driver


def build_route(route_number, time, capacity, driver):
    route_number = normalize_route_number(route_number)
    time = normalize_time(time)
    capacity = normalize_capacity(capacity)
    driver = normalize_driver(driver)

    if route_number is None:
        raise BusRouteValidationError(None, "Номер рейса обязателен.")
    if time is None:
        raise BusRouteValidationError(route_number, "Время отправления обязательное.")
    if capacity is None:
        raise BusRouteValidationError(route_number, "Вместимость должна быть положительным числом.")
    if driver is None:
        raise BusRouteValidationError(route_number, "Водитель обязателен.")

    return route_number, time, capacity, driver
