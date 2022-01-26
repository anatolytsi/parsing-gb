# Lesson 3. MongoDB and SQLite Database Control Systems in Python
### Create a MondoDB database and allow adding only new vacancies there. Make a function to find salary which is greater than a given value.

##### Run script:

A script entry point is file `db_parser.py`

##### Functionality:

Script parses vacancies for position "Разработчик" from [hh.ru](https://hh.ru) and [superjob.ru](https://superjob.ru) websites by default. Maximum amount of pages is parsed for each website using [BeautifulSoup](https://pypi.org/project/beautifulsoup4/), then saved to a DB.

###### Example input:
```commandline
Enter a currency. Possible currencies are EUR, KZT, USD, руб or skip for any: руб
Enter a minimal salary for search: 250000
```

###### Example output using pretty-print:
```json
[{'Currency': 'руб',
  'Maximum Salary': 350000,
  'Minimum Salary': 200000,
  'Position': 'Python Developer',
  'URL': 'https://hh.ru/vacancy/51160196?from=vacancy_search_list&hhtmFrom=vacancy_search_list&query=Python',
  'Website': 'hh.ru',
  '_id': ObjectId('61f1ac9989ea4d5e2df93a37')},
 {'Currency': 'руб',
  'Maximum Salary': '',
  'Minimum Salary': 300000,
  'Position': 'Data scientist',
  'URL': 'https://hh.ru/vacancy/51710392?from=vacancy_search_list&hhtmFrom=vacancy_search_list&query=Python',
  'Website': 'hh.ru',
  '_id': ObjectId('61f1ac9989ea4d5e2df93a45')},
 {'Currency': 'руб',
  'Maximum Salary': 300000,
  'Minimum Salary': 250000,
  'Position': 'Middle\xa0Data\xa0Science',
  'URL': 'https://hh.ru/vacancy/51365940?from=vacancy_search_list&hhtmFrom=vacancy_search_list&query=Python',
  'Website': 'hh.ru',
  '_id': ObjectId('61f1ac9989ea4d5e2df93a47')},
 {'Currency': 'руб',
  'Maximum Salary': 515000,
  'Minimum Salary': 300000,
  'Position': 'DevOps инженер',
  'URL': 'https://hh.ru/vacancy/51112762?from=vacancy_search_list&hhtmFrom=vacancy_search_list&query=Python',
  'Website': 'hh.ru',
  '_id': ObjectId('61f1ac9989ea4d5e2df93a4d')},
 ...
```

