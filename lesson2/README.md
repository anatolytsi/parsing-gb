# Lesson 2. HTML Parsing. BeautifulSoup
### Collect vacancies information from hh.ru and superjob.ru.

##### Run script:

A script entry point is file `parser.py`

##### Functionality:

Script parses vacancies for position "Разработчик" from [hh.ru](https://hh.ru) and [superjob.ru](https://superjob.ru) websites by default. Two pages are parsed for each website using [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), concatenated into a single dataframe and saved as [collected_data.csv](collected_data.csv).

###### Collected data example:

|Position                    |URL                                                  |Min. Salary|Max. Salary|Currency|Website    |
|----------------------------|-----------------------------------------------------|-----------|-----------|--------|-----------|
|Ведущий разработчик С++/Qt  |superjob.ru/vakansii/veduschij-razrabotchik-s-41309095.html|           |120000     |руб     |superjob.ru|
|Программист 1С              |superjob.ru/vakansii/programmist-1s-40974649.html    |120000     |130000     |руб     |superjob.ru|
|Frontend developer (VUE)    |superjob.ru/vakansii/frontend-developer-40902995.html|           |           |        |superjob.ru|
|Frontend Developer (ReactJS)|superjob.ru/vakansii/frontend-developer-40903075.html|           |           |        |superjob.ru|
|Программист SQL (OLAP-кубы) |superjob.ru/vakansii/programmist-sql-41200654.html   |150000     |           |руб     |superjob.ru|
|Программист PLC             |superjob.ru/vakansii/programmist-plc-41306259.html   |80000      |100000     |руб     |superjob.ru|
|...                         |...                                                  |...        |...        |...     |...        |

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
    pages_t = 'a.bloko-button[data-qa=pager-page] span'
    container_t = 'div.vacancy-serp-item'
    position_t = 'a[data-qa=vacancy-serp__vacancy-title]'
    url_t = 'a[data-qa=vacancy-serp__vacancy-title]'
    salary_t = 'span.bloko-header-section-3[data-qa=vacancy-serp__vacancy-compensation]'
    requester = lambda page: requests.get(f'{PROT}{HH_URL}/search/vacancy',
                                          params={'text': position, 'page': page},
                                          headers=HEADERS)
    df = get_vacancies_from_pages(HH_URL, pages, requester, pages_t, container_t, position_t, url_t, salary_t)
    return df
```
