import sqlite3
import os
from collections.abc import Collection
from typing import Iterator


class TableData(Collection):
    """Класс для работы с таблицей SQLite как с коллекцией"""

    def __init__(self, database_name: str, table_name: str):
        """Инициализация с проверкой существования файла БД"""
        if not os.path.exists(database_name):
            raise FileNotFoundError(
                f"DB file '{database_name}' not found")
        self.database_name = database_name
        self.table_name = table_name

    def _execute_query(self, query: str, params: dict = None):
        """Выполняет SQL-запрос и возвращает курсор"""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or {})
            return cursor

    def __len__(self) -> int:
        """Возвращает количество строк в таблице."""
        return self._execute_query(f"SELECT COUNT(*) FROM {self.table_name}").fetchone()[0]

    def __getitem__(self, name: str):
        """Возвращает запись по имени или выбрасывает KeyError"""
        row = self._execute_query(
            f"SELECT * FROM {self.table_name} WHERE name = :name", {"name": name}).fetchone()
        if row is None:
            raise KeyError(f"No entry found for: {name}")
        return row

    def __contains__(self, name: str) -> bool:
        """Проверяет наличие записи с указанным именем"""
        return bool(self._execute_query(f"SELECT EXISTS(SELECT 1 FROM {self.table_name} WHERE name = :name)", {"name": name}).fetchone()[0])

    def __iter__(self) -> Iterator:
        """Итерируется по записям таблицы"""
        cursor = self._execute_query(f"SELECT * FROM {self.table_name}")
        while row := cursor.fetchone():
            yield row
