from pathlib import Path

HH_URL = "https://api.hh.ru/vacancies"
SJ_URL = "https://api.superjob.ru/2.0/vacancies"

PARENT_PATH = Path(__file__).parent
PATH_TO_JSON = Path(PARENT_PATH, "vacancies.json")
