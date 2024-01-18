from config import PATH_TO_JSON
from src.api import HeadHunterAPI, SuperJobAPI
from src.files import FileSaverJSON
from src.utils import create_hh_instances, create_sj_instances, sort_by_salary, convert_to_instance


def main():
    search_query = input("Введите поисковый запрос:\n")
    platform_query = input('Введите название платформы для поиска\n(Доступны "HH" / "SJ")\n').rstrip().lstrip()
    currency_query = input('Введите валюту зарплаты:\n').rstrip().lstrip().upper()
    town_query = input('Введите город:\n').rstrip().lstrip().capitalize()
    page_query = input('Введите, на какой странице платформы искать (1 - 10):\n')
    try:
        page_num = int(page_query) - 1
    except ValueError:
        page_num = None

    hh_api = HeadHunterAPI(search_query)
    sj_api = SuperJobAPI(search_query)

    hh_api_vacancies = hh_api.get_data(page_num)
    sj_api_vacancies = sj_api.get_data(page_num)

    hh_instances = create_hh_instances(hh_api_vacancies)
    sj_instances = create_sj_instances(sj_api_vacancies)

    saver = FileSaverJSON(PATH_TO_JSON)
    saver.add_vacancies(hh_instances + sj_instances)

    filter_of_vacancies = {}
    if platform_query in ("HH", "SJ"):
        filter_of_vacancies["platform"] = platform_query
    if currency_query != "":
        filter_of_vacancies["currency"] = currency_query
    if town_query != "":
        filter_of_vacancies["town"] = town_query

    filtered_vacancies = saver.get_vacancies(filter_of_vacancies)
    sorted_vacancies = sort_by_salary(convert_to_instance(filtered_vacancies))
    if not sorted_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    top_n = int(input("Введите количество вакансий для вывода в топ N:\n"))
    for vacancy in sorted_vacancies[:top_n]:
        print(vacancy)


if __name__ == "__main__":
    main()
