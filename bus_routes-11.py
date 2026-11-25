# === Stage 11: Текстовый поиск ===
# Project: BusRoutes
def find_trips(trips, query):
    """Поиск рейсов по текстовым полям без учёта регистра с подсветкой совпадений.

    Ищет в полях номер и водитель. Совпадения выделяются обратными кавычками.
    """
    query = query.strip().lower()
    if not query:
        return []

    def highlight(value):
        if not value:
            return value
        parts = []
        index = 0
        lower = value.lower()
        start = None
        while True:
            pos = lower.find(query, index)
            if pos == -1:
                if start is not None:
                    parts.append(value[start:])
                break
            if start is None:
                start = pos
            parts.append(value[index:start])
            parts.append("`" + value[pos:pos + len(query)] + "`")
            index = pos + len(query)
        return "".join(parts)

    results = []
    for trip in trips:
        number = trip.get("number", "")
        driver = trip.get("driver", "")
        if query in number.lower() or query in driver.lower():
            results.append({
                "number": highlight(number),
                "driver": highlight(driver),
                "time": trip.get("time", ""),
                "capacity": trip.get("capacity", ""),
            })
    return results


def demo():
    sample = [
        {"number": "A-101", "time": "07:30", "capacity": 30, "driver": "Иванов"},
        {"number": "B-202", "time": "08:15", "capacity": 25, "driver": "Петров"},
        {"number": "C-303", "time": "09:45", "capacity": 40, "driver": "Сидоров"},
    ]
    for q in ["иванов", "a-101", "202", ""]:
        print(f"Запрос: {q!r}")
        for r in find_trips(sample, q):
            print(f"  {r['number']} | {r['time']} | водитель: {r['driver']} | вместимость: {r['capacity']}")
        print()


if __name__ == "__main__":
    demo()
