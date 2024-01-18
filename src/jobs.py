class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ["vacancy_name", "salary_from", "salary_to", "currency", "town", "url", "str", "average_salary"]

    def __init__(self, vacancy_name: str, salary_from, salary_to, currency: str, town: str, url: str):
        self.vacancy_name: str = vacancy_name.capitalize()
        self.salary_from: int = self.validate_salary(salary_from)
        self.salary_to: int = self.validate_salary(salary_to)
        self.currency: str = self.validate_currency(currency)
        self.town: str = town
        self.url: str = url
        self.str: str = (f"{self.vacancy_name} (от {self.salary_from} до {self.salary_to} {self.currency}) "
                         f"в {self.town}: {self.url}")
        self.average_salary: int = self.validate_average_salary()

    def __str__(self):
        return f"Вакансия {self.str}"

    def __gt__(self, other):
        return self.average_salary > other.average_salary

    def __lt__(self, other):
        return self.average_salary < other.average_salary

    def __eq__(self, other):
        return self.average_salary == other.average_salary

    def validate_average_salary(self) -> int:
        """
        Возвращает среднюю зарплату в вакансии, если указан зарплатный диапазон,
        иначе возвращает указанное в вакансии значение,
        возвращает 0, если зарплата не указана
        """
        if self.salary_from > 0 and self.salary_to > 0:
            return int((self.salary_from + self.salary_to) / 2)
        elif self.salary_from > 0 and self.salary_to == 0:
            return self.salary_from
        elif self.salary_from == 0 and self.salary_to > 0:
            return self.salary_to
        elif self.salary_from == 0 and self.salary_to == 0:
            return 0

    def write_to_dict(self) -> dict:
        return {
            "vacancy_name": self.vacancy_name,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency,
            "town": self.town,
            "url": self.url
        }

    @staticmethod
    def validate_salary(salary) -> int:
        """Возвращает 0, если зарплата не указана"""
        try:
            if salary is None:
                return 0
        except TypeError:
            return 0
        else:
            return salary

    @staticmethod
    def validate_currency(currency) -> str:
        """Возвращает название валюты"""
        if currency.lower() in ("rur", "rub"):
            return "RUB"
        else:
            return currency.upper()


class HeadHunterVacancy(Vacancy):
    """Класс для работы с вакансиями с hh.ru"""
    platform_name = "HH"

    def __str__(self):
        return f"Вакансия на HeadHunter {self.str}"

    def write_to_dict(self) -> dict:
        vacancy_dict = super().write_to_dict()
        vacancy_dict["platform"] = self.platform_name
        return vacancy_dict


class SuperJobVacancy(Vacancy):
    """Класс для работы с вакансиями с SuperJob.ru"""
    platform_name = "SJ"

    def __str__(self):
        return f"Вакансия на SuperJob {self.str}"

    def write_to_dict(self) -> dict:
        vacancy_dict = super().write_to_dict()
        vacancy_dict["platform"] = self.platform_name
        return vacancy_dict
