# === Stage 4: Редактирование записей ===
# Project: BusRoutes
class BusRoute:
    def __init__(self, route_number, departure_time, capacity, driver):
        self.route_number = route_number
        self.departure_time = departure_time
        self.capacity = capacity
        self.driver = driver

    def update(self, route_number=None, departure_time=None, capacity=None, driver=None):
        valid_fields = {
            'route_number': self.route_number,
            'departure_time': self.departure_time,
            'capacity': self.capacity,
            'driver': self.driver,
        }
        for field, value in self.__validate_update(route_number, departure_time, capacity, driver).items():
            if value is not None:
                valid_fields[field] = value
        return BusRoute(**valid_fields)

    def __validate_update(self, route_number, departure_time, capacity, driver):
        updates = {}
        if route_number is not None:
            if not isinstance(route_number, str) or len(route_number) == 0:
                raise ValueError('route_number должен быть непустой строкой')
            updates['route_number'] = route_number
        if departure_time is not None:
            if not isinstance(departure_time, str):
                raise ValueError('departure_time должен быть строкой')
            updates['departure_time'] = departure_time
        if capacity is not None:
            if not isinstance(capacity, int) or capacity <= 0:
                raise ValueError('capacity должен быть положительным целым числом')
            updates['capacity'] = capacity
        if driver is not None:
            if not isinstance(driver, str) or len(driver) == 0:
                raise ValueError('driver должен быть непустой строкой')
            updates['driver'] = driver
        return updates
