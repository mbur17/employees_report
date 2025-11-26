from typing import Any, Dict, Iterable, List


class BaseReport():
    """Базовый класс для всех отчётов."""
    name: str = ""  # Идентификатор отчета (для --report).
    headers: List[str] = []  # Заголовки колонок результирующей таблицы.

    def build(self, rows: Iterable[Dict[str, Any]]) -> List[List[Any]]:
        """Сформировать строки отчета."""
        raise NotImplementedError
