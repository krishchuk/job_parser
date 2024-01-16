from src.jobs import HeadHunterVacancy, SuperJobVacancy, Vacancy


def create_hh_instances(vacancies: list[dict]) -> list[Vacancy]:
    all_vacancies = []
    for vacancy in vacancies:
        try:
            salary_from = vacancy["salary"]["from"]
        except TypeError:
            salary_from = 0
        try:
            salary_to = vacancy["salary"]["to"]
        except TypeError:
            salary_to = 0
        try:
            currency = vacancy["salary"]["currency"]
        except TypeError:
            currency = ""
        try:
            town = vacancy["area"]["name"]
        except TypeError:
            town = ""
        hh_vacancy = HeadHunterVacancy(
            vacancy_name=vacancy["name"],
            salary_from=salary_from,
            salary_to=salary_to,
            currency=currency,
            town=town,
            url=vacancy["url"]
        )
        all_vacancies.append(hh_vacancy)
    return all_vacancies


def create_sj_instances(vacancies: list[dict]) -> list[Vacancy]:
    all_vacancies = []
    for vacancy in vacancies:
        try:
            town = vacancy["town"]["title"]
        except TypeError:
            town = ""
        sj_vacancy = SuperJobVacancy(
            vacancy_name=vacancy["profession"],
            salary_from=vacancy["payment_from"],
            salary_to=vacancy["payment_to"],
            currency=vacancy["currency"],
            town=town,
            url=vacancy["link"]
        )
        all_vacancies.append(sj_vacancy)
    return all_vacancies


def sort_by_salary(vacancies: list) -> list[Vacancy]:
    return sorted(vacancies, reverse=True)


def convert_to_instance(vacancies: list[dict]) -> list[Vacancy]:
    instances = []
    for vacancy in vacancies:
        if vacancy["platform"] == "HH":
            instances.append(HeadHunterVacancy(**vacancy))
        elif vacancy["platform"] == "SJ":
            instances.append(SuperJobVacancy(**vacancy))
    return instances
