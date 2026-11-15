# === Stage 6: Связанная сущность ===
# Project: BusRoutes
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Stop:
    id: str
    name: str
    address: str = ""
    is_active: bool = True

    def __post_init__(self):
        if not self.id or not isinstance(self.id, str):
            raise ValueError("stop id must be a non-empty string")
        self.id = self.id.strip()
        if not self.name:
            raise ValueError("stop name must not be empty")

    def __repr__(self):
        return f"Stop(id={self.id!r}, name={self.name!r})"


@dataclass
class RouteStop:
    stop_id: str
    route_id: str
    order: int
    arrival_time: Optional[str] = None
    departure_time: Optional[str] = None

    def __post_init__(self):
        if not self.stop_id or not self.route_id:
            raise ValueError("stop_id and route_id must be non-empty")
        if self.order < 0:
            raise ValueError("order must be non-negative")


@dataclass
class StopRegistry:
    _stops: Dict[str, Stop] = field(default_factory=dict)

    def register(self, stop: Stop) -> Stop:
        self._stops[stop.id] = stop
        return stop

    def get(self, stop_id: str) -> Optional[Stop]:
        return self._stops.get(stop_id)

    def find_by_name(self, name: str) -> Optional[Stop]:
        for stop in self._stops.values():
            if stop.name.lower() == name.lower():
                return stop
        return None

    def active_count(self) -> int:
        return sum(1 for s in self._stops.values() if s.is_active)

    def to_dict(self) -> Dict[str, dict]:
        return {sid: {"id": s.id, "name": s.name, "address": s.address, "is_active": s.is_active}
                for sid, s in self._stops.items()}

    def __len__(self):
        return len(self._stops)


def parse_route_stops(spec: str, route_id: str, registry: StopRegistry) -> List[RouteStop]:
    stops: List[RouteStop] = []
    for line in spec.strip().splitlines():
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 3:
            continue
        stop_id, order = parts[0], int(parts[1])
        arrival, departure = parts[2], parts[3] if len(parts) > 3 else None
        if registry.get(stop_id) is None:
            continue
        stops.append(RouteStop(stop_id=stop_id, route_id=route_id, order=order,
                               arrival_time=arrival, departure_time=departure))
    stops.sort(key=lambda s: s.order)
    return stops


if __name__ == "__main__":
    reg = StopRegistry()
    reg.register(Stop(id="s1", name="ул. Ленина 1"))
    reg.register(Stop(id="s2", name="Школа №5"))
    reg.register(Stop(id="s3", name="Парк"))

    print("active stops:", reg.active_count())
    print(parse_route_stops("s1|0|08:00|\ns2|1|08:05|\nunknown|2|\ns3|3|08:10|", "r1", reg))
