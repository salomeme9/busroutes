# === Stage 8: Генерация идентификаторов ===
# Project: BusRoutes
import uuid
from typing import List


PROJECT_PREFIX = "busr"


def generate_unique_id() -> str:
    """Генерирует уникальный идентификатор с префиксом проекта."""
    candidate = f"{PROJECT_PREFIX}-{uuid.uuid4().hex}"
    if not check_collision(candidate):
        return candidate
    raise ValueError("Не удалось сгенерировать уникальный ID")


def check_collision(candidate: str, existing: List[str]) -> bool:
    """Проверяет, существует ли ID в списке уже использованных."""
    return candidate in existing


def generate_unique_id_with_check(
    prefix: str = PROJECT_PREFIX,
    existing: List[str] | None = None,
) -> str:
    """Генерирует уникальный ID, проверяя коллизии с переданным списком."""
    used = set(existing or [])
    while True:
        candidate = f"{prefix}-{uuid.uuid4().hex}"
        if candidate not in used:
            return candidate
        used.add(candidate)


def assign_unique_ids(items: List[dict]) -> List[dict]:
    """Добавляет поле id к каждому элементу списка, без коллизий."""
    used: List[str] = []
    for item in items:
        new_id = generate_unique_id_with_check(existing=used)
        used.append(new_id)
        item["id"] = new_id
    return items


def unique_id_counter(prefix: str = PROJECT_PREFIX) -> int:
    """Генерирует последовательные уникальные ID без случайности."""
    counter = 0
    while True:
        candidate = f"{prefix}-{counter}"
        counter += 1
        if not check_collision(candidate):
            return candidate
