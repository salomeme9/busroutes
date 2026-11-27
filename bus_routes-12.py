# === Stage 12: Поиск по нескольким словам ===
# Project: BusRoutes
def find_trips(query, trips):
    """Поиск рейсов по нескольким словам с поддержкой исключений через префикс '-'.

    Токены без дефиса — обязательные для совпадения слова (поиск по подстроке в
    номере/времени/вместимости/водителе). Токены с дефисом — слова, которые должны
    отсутствовать в рейсе. Рейс отбирается, если он содержит все обязательные и не
    содержит ни одного исключённого слова.
    """
    tokens = query.replace('-', ' - ').split(' ')
    tokens = [t for t in tokens if t.strip()]
    required = [t for t in tokens if not t.startswith('-')]
    excluded = [t[1:] for t in tokens if t.startswith('-')]

    def contains(trip, word):
        haystack = ' '.join(
            [str(trip.number), str(trip.time),
             str(trip.capacity), str(trip.driver)]
        ).lower()
        return word in haystack

    return [trip for trip in trips
            if all(contains(trip, w) for w in required)
            if not any(excluded and not contains(trip, w) for w in excluded)]


class Trip:
    def __init__(self, number, time, capacity, driver):
        self.number = number
        self.time = time
        self.capacity = capacity
        self.driver = driver

    def __repr__(self):
        return 'Trip(%r, %r, %r, %r)' % (
            self.number, self.time, self.capacity, self.driver
        )


if __name__ == '__main__':
    demo_trips = [
        Trip('A1', '08:00', 30, 'Иванов'),
        Trip('B2', '08:30', 25, 'Петров'),
        Trip('C3', '09:15', 40, 'Сидоров'),
        Trip('A1', '17:00', 30, 'Иванов'),
    ]
    print(find_trips('A1 Иванов', demo_trips))
    print(find_trips('-Сидоров', demo_trips))
    print(find_trips('A1 -Иванов', demo_trips))
