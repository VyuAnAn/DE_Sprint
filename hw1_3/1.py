# -*- coding: utf-8 -*-
"""
Необходимо спарсить данные о вакансиях python разработчиков с сайта hh.ru,
введя в поиск “python разработчик” и указав, что мы рассматриваем все регионы. Необходимо спарсить:

Название вакансии
Требуемый опыт работы
Заработную плату
Регион
И сохранить эти данные в формате json
"""
import time

import requests
import tqdm
from bs4 import BeautifulSoup
import json

url = "https://hh.ru"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

data = {
    "data": []
}

page = 1

while True:
    search_string = f"/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&area=&page={page}&hhtmFrom=vacancy_search_list&items_on_page=100"

    try:
        response = requests.get(url=url + search_string, headers=headers)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "lxml")
        vacancies = soup.find_all(class_="vacancy-serp-item-body__main-info")

        for vacancy in tqdm.tqdm(vacancies):
            vacancy_info = vacancy.find(class_="serp-item__title")

            response_vacancy = requests.get(url=vacancy_info.attrs["href"], headers=headers)
            soup_vacancy = BeautifulSoup(response_vacancy.text, "lxml")

            vacancy_salary = soup_vacancy.find(attrs={"data-qa": "vacancy-salary-compensation-type-net"})
            vacancy_salary = vacancy_salary.text if vacancy_salary else 'Не указана'

            data["data"].append({
                "title": vacancy_info.text,
                "work experience": soup_vacancy.find(attrs={"data-qa": "vacancy-experience"}).text,
                "salary": vacancy_salary,
                "region": vacancy.find(attrs={"data-qa": "vacancy-serp__vacancy-address"}).text
            })

            with open("data.json", "w") as file:
                json.dump(data, file, ensure_ascii=False)

        page += 1
        time.sleep(3)

    except Exception as err:
        print(err)
        break
