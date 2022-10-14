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
cnt = 0
while True:
    search_string = f"/search/vacancy?no_magic=true&L_save_area=true&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&page={page}&hhtmFrom=vacancy_search_list"

    try:
        response = requests.get(url=url + search_string, headers=headers)

        if response.status_code != 200:
            print(response)
            break

        soup = BeautifulSoup(response.text, "lxml")
        vacancies = soup.find_all(class_="vacancy-serp-item-body__main-info")

        for vacancy in tqdm.tqdm(vacancies):

            vacancy_info = vacancy.find(class_="serp-item__title")

            response_vacancy = requests.get(url=vacancy_info.attrs["href"], headers=headers)
            soup_vacancy = BeautifulSoup(response_vacancy.text, "lxml")

            vacancy_salary = soup_vacancy.find(attrs={"data-qa": "vacancy-salary-compensation-type-net"})
            vacancy_salary = vacancy_salary.text if vacancy_salary else 'Не указана'

            work_experience = soup_vacancy.find(attrs={"data-qa": "vacancy-experience"})
            work_experience = work_experience.text if work_experience else 'Не указан'

            region = vacancy.find(attrs={"data-qa": "vacancy-serp__vacancy-address"})
            region = region.text if region else 'Не указан'

            data["data"].append({
                "title": vacancy_info.text,
                "work experience": work_experience,
                "salary": vacancy_salary,
                "region": region
            })
            cnt += 1
            with open("data.json", "w") as file:
                json.dump(data, file, ensure_ascii=False)

        print('page %s(%s)' % (page, cnt))
        page += 1
        time.sleep(3)

    except Exception as err:
        print(err)
        break


print(cnt)
