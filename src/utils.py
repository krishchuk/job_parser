from src.jobs import HeadHunterVacancy, SuperJobVacancy, Vacancy


def create_hh_instances(vacancies: list[dict]) -> list[Vacancy]:
    all_vacancies = []
    for vacancy in vacancies:
        sj_vacancy = HeadHunterVacancy(
            vacancy_name=vacancy["name"],
            salary_from=vacancy["salary"]["from"],
            salary_to=vacancy["salary"]["to"],
            currency=vacancy["salary"]["currency"],
            town=vacancy["area"]["name"],
            url=vacancy["url"]
        )
        all_vacancies.append(sj_vacancy)
    return all_vacancies


def create_sj_instances(vacancies: list[dict]) -> list[Vacancy]:
    all_vacancies = []
    for vacancy in vacancies:
        sj_vacancy = SuperJobVacancy(
            vacancy_name=vacancy["profession"],
            salary_from=vacancy["payment_from"],
            salary_to=vacancy["payment_to"],
            currency=vacancy["currency"],
            town=vacancy["town"]["title"],
            url=vacancy["link"]
        )
        all_vacancies.append(sj_vacancy)
    return all_vacancies
