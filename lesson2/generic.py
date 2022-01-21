from typing import Callable

import requests
from bs4 import BeautifulSoup
import pandas as pd

POSITIONS_K = 'POSITION'
URL_K = 'URL'
SALARY_K = 'Salary'
WEBSITE_K = 'Website'


def vacancy_parser(response: requests.Response,
                   container_t: str,
                   position_t: str,
                   url_t: str,
                   salary_t: str) -> tuple:
    """

    :param response: website get response to a
        vacancy list.
    :param container_t: BeautifulSoup select
        string for vacancy card container.
    :param position_t: BeautifulSoup select
        string for position container.
    :param url_t: BeautifulSoup select
        string for URL container.
    :param salary_t: BeautifulSoup select
        string for salary container.
    :return: positions, urls, salaries lists
    """
    dom = BeautifulSoup(response.text, 'html.parser')
    vacancies = dom.select(container_t)
    positions, urls, salaries = [], [], []
    for vacancy in vacancies:
        position = vacancy.select_one(position_t).get_text()
        url = vacancy.select_one(url_t).get('href')
        salary = tag.get_text() if (tag := vacancy.select_one(salary_t)) else ''
        positions.append(position)
        urls.append(url)
        salaries.append(salary)
    return positions, urls, salaries


def get_vacancies_from_pages(website_url: str,
                             pages: int,
                             requester: Callable,
                             container_t: str,
                             position_t: str,
                             url_t: str,
                             salary_t: str) -> pd.DataFrame:
    """
    Gets certain positions from a given
    website within a number of pages and
    returns them as a DataFrame.

    :param website_url: website to collect data.
    :param pages: amount of pages to cover.
    :param requester: function to request data
        with page as argument.
    :param container_t: BeautifulSoup select
        string for vacancy card container.
    :param position_t: BeautifulSoup select
        string for position container.
    :param url_t: BeautifulSoup select
        string for URL container.
    :param salary_t: BeautifulSoup select
        string for salary container.
    :return: pandas DataFrame
    """
    vacancies = {POSITIONS_K: [], URL_K: [], SALARY_K: []}
    for page in range(1, pages):
        response = requester(page)
        positions, urls, salaries = vacancy_parser(response, container_t, position_t, url_t, salary_t)
        vacancies[POSITIONS_K].extend(positions)
        vacancies[URL_K].extend([f'{website_url}{url}' if website_url not in url else url for url in urls])
        vacancies[SALARY_K].extend(salaries)
    df = pd.DataFrame(vacancies)
    df[WEBSITE_K] = website_url
    return df
