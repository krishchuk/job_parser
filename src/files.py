import json
from abc import ABC, abstractmethod

from src.jobs import Vacancy


class FileSaver(ABC):
    """Абстрактный класс для работы с файлом"""
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, queries=None) -> list[dict]:
        pass

    @abstractmethod
    def del_vacancies(self, queries=None) -> None:
        pass


class FileSaverJSON(FileSaver):
    """Класс для работы с файлом JSON"""

    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        vacancies_json = [vacancy.write_to_dict() for vacancy in vacancies]
        with open(self.path, "r", encoding="utf-8") as file:
            old_vacancies: list[dict] = json.load(file)
        old_vacancies.extend(vacancies_json)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(old_vacancies, file)

    def get_vacancies(self, queries=None) -> list[dict]:
        with open(self.path, "r", encoding="utf-8") as file:
            all_vacancies: list[dict] = json.load(file)
        vacancies = []
        for vacancy in all_vacancies:
            if all(vacancy.get(field) == query for field, query in queries.items()):
                vacancies.append(vacancy)
        return vacancies

    def del_vacancies(self, queries=None) -> None:
        vacancies_to_del = self.get_vacancies(queries)
        with open(self.path, "r", encoding="utf-8") as file:
            all_vacancies: list[dict] = json.load(file)
        vacancies = []
        for vacancy in all_vacancies:
            if vacancy not in vacancies_to_del:
                vacancies.append(vacancy)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file)
