# Lesson 6. Scrapy
### Collect vacancies information from [hh.ru](https://hh.ru) and [superjob.ru](https://superjob.ru) using [Scrapy](https://scrapy.org/) and save them to DB.

##### Run script:

To parse hh.ru run `scrapy crawl hhru`
To parse superjob.ru run `scrapy crawl superjob`

###### Collected data example:
```json
[
  {
    "_id": {
      "$oid": "61fd9e78cafcddbe6dec4bb8"
    },
    "position": "Backend-разработчик Python + Django (Middle/Senior)",
    "url": "https://hh.ru/vacancy/50999248?from=vacancy_search_list&hhtmFrom=vacancy_search_list&query=python",
    "salary_min": 180000,
    "salary_max": 230000,
    "currency": "руб"
  },
  {
    "_id": {
      "$oid": "61fd9ec7cafcddbe6dec4bd3"
    },
    "position": "Специалист по тестированию",
    "url": "https://hh.ru/vacancy/40585500?from=vacancy_search_list&hhtmFrom=vacancy_search_list&query=python",
    "salary_min": "",
    "salary_max": "",
    "currency": ""
  }
]
```
