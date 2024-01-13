import os
from abc import ABC, abstractmethod

import requests
from dotenv import load_dotenv

from config import HH_URL, SJ_URL


load_dotenv()


class API(ABC):
    """Абстрактный класс для получения данных через API"""
    @abstractmethod
    def get_data(self) -> list[dict]:
        pass


class HeadHunterAPI(API):
    """Класс для получения данных с hh.ru через API"""
    def __init__(self, query: str) -> None:
        self.query = query
        self.params = {
            "text": self.query,
            "per_page": 100
        }

    def get_data(self, page=0) -> list[dict]:
        self.params["page"] = page
        return requests.get(url=HH_URL, params=self.params).json()["items"]


class SuperJobAPI(API):
    """Класс для получения данных с superjob.ru через API"""
    def __init__(self, query: str) -> None:
        self.query = query
        self.params = {
            "keyword": self.query,
            "count": 100
        }

    def get_data(self, page=0) -> list[dict]:
        self.params["page"] = page
        headers = {
            "X-Api-App-Id": os.getenv("SJ_API_KEY")
        }
        return requests.get(url=SJ_URL, params=self.params, headers=headers).json()["objects"]
