import json
from abc import ABC, abstractmethod

from src.jobs import Vacancy


class FileSaver(ABC):
    """Абстрактный класс для работы с файлом"""
    def __init__(self, path):
        self.path = path
        self.write_json([])

    @abstractmethod
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, queries=None) -> list[dict]:
        pass

    @abstractmethod
    def del_vacancies(self, queries=None) -> None:
        pass

    def read_json(self) -> list[dict]:
        with open(self.path, "r", encoding="utf-8") as file:
            vacancies: list[dict] = json.load(file)
        return vacancies

    def write_json(self, vacancies: list) -> None:
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)


class FileSaverJSON(FileSaver):
    """Класс для работы с файлом JSON"""

    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        vacancies_json = [vacancy.write_to_dict() for vacancy in vacancies]
        old_vacancies = self.read_json()
        old_vacancies.extend(vacancies_json)
        self.write_json(old_vacancies)

    def get_vacancies(self, queries=None) -> list[dict]:
        all_vacancies = self.read_json()
        vacancies = []
        for vacancy in all_vacancies:
            if all(vacancy.get(field) == query for field, query in queries.items()):
                vacancies.append(vacancy)
        return vacancies

    def del_vacancies(self, queries=None) -> None:
        vacancies_to_del = self.get_vacancies(queries)
        all_vacancies = self.read_json()
        vacancies = []
        for vacancy in all_vacancies:
            if vacancy not in vacancies_to_del:
                vacancies.append(vacancy)
        self.write_json(vacancies)
