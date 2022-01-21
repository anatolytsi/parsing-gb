"""
Collect vacancies information from hh.ru and superjob.ru.
"""
import requests
import pandas as pd

from lesson2.generic import get_vacancies_from_pages

HH_URL = 'hh.ru'
SJ_URL = 'superjob.ru'
PROT = 'https://'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'
}


def get_hh_vacancies(position: str, pages: int = 2) -> pd.DataFrame:
    """
    Gets certain positions from hh.ru from a number
    of pages and returns them as a DataFrame.

    :param position: name of a vacancy to search.
    :param pages: amount of pages to cover.
    :return: pandas DataFrame.
    """
    container_t = 'div.vacancy-serp-item'
    position_t = 'a[data-qa=vacancy-serp__vacancy-title]'
    url_t = 'a[data-qa=vacancy-serp__vacancy-title]'
    salary_t = 'span.bloko-header-section-3[data-qa=vacancy-serp__vacancy-compensation]'
    requester = lambda page: requests.get(f'{PROT}{HH_URL}/search/vacancy',
                                          params={'text': position, 'page': page},
                                          headers=HEADERS)
    df = get_vacancies_from_pages(HH_URL, pages, requester, container_t, position_t, url_t, salary_t)
    return df


def get_superjob_vacancies(position: str, pages: int = 2) -> pd.DataFrame:
    """
    Gets certain positions from superjob.ru from a number
    of pages and returns them as a DataFrame.

    :param position: name of a position to search.
    :param pages: amount of pages to cover.
    :return: pandas DataFrame.
    """
    container_t = 'div.f-test-vacancy-item'
    position_t = 'a'
    url_t = 'a'
    salary_t = 'span.f-test-text-company-item-salary span'
    requester = lambda page: requests.get(f'{PROT}{SJ_URL}/vacancy/search/',
                                          params={'keywords': position, 'page': page},
                                          headers=HEADERS)
    df = get_vacancies_from_pages(SJ_URL, pages, requester, container_t, position_t, url_t, salary_t)
    return df


def main():
    position = 'Разработчик'
    hh_df = get_hh_vacancies(position)
    sj_df = get_superjob_vacancies(position)
    websites_df = pd.concat([hh_df, sj_df])
    websites_df.to_csv('collected_data.csv', index=False)


if __name__ == '__main__':
    main()
