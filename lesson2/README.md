# Lesson 2. HTML Parsing. BeautifulSoup
### Collect vacancies information from hh.ru and superjob.ru.

##### Run script:

A script entry point is file `parser.py`

##### Functionality:

Script parses vacancies for position "Разработчик" from [hh.ru](https://hh.ru) and [superjob.ru](https://superjob.ru) websites by default. Two pages are parsed for each website using [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), concatenated into a single dataframe and saved as [collected_data.csv](collected_data.csv).

###### Collected data example:

|Position                       |URL                                                                                                                                                          |Salary    |Website|
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|
|Разработчик .NET (#C)          |https://hh.ru/vacancy/51256477?from=vacancy_search_list&query=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&hhtmFrom=vacancy_search_list|          |hh.ru  |
|Dart/Flutter Developer         |https://hh.ru/vacancy/48345898?from=vacancy_search_list&query=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&hhtmFrom=vacancy_search_list|от 2 000 EUR|hh.ru  |
|PHP разработчик (на Кипр)      |https://hh.ru/vacancy/51335330?from=vacancy_search_list&query=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&hhtmFrom=vacancy_search_list|          |hh.ru  |
|Frontend разработчик           |https://hh.ru/vacancy/50691684?from=vacancy_search_list&query=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&hhtmFrom=vacancy_search_list|120 000 – 200 000 руб.|hh.ru  |
|...                            |...                                                                                                                                                          |...       |...    |

##### [hh.ru](https://hh.ru) (example) function overview:

```python
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
```
