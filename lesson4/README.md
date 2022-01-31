# Lesson 4. HTML Parsing. XPath
### Create an app to parse news from websites ([news.mail.ru](https://news.mail.ru/), [lenta.ru](https://lenta.ru/), [yandex-новости](https://yandex.ru/news/)) using XPath. The structure should contain: source name, news title, news link, publication date. Put data into database.

##### Run script:

A script entry point is file `news_parser.py`

##### Functionality:

Script parses news from given webistes, then saves results to a DB.

###### Collected data example:
```json
[
  {
    "title": "Над США заметили тройной зеленый луч",
    "url": "https://news.mail.ru/incident/49797916/",
    "source": "Коммерсантъ",
    "date": "27.01.2022 22:34:24"
  },
  {
    "title": "Лукашенко назвал два условия начала войны",
    "url": "https://news.mail.ru/society/49810053/",
    "source": "RTVi",
    "date": "28.01.2022 16:10:07"
  },
  {
    "title": "Выход есть.",
    "url": "https://lenta.ru/articles/2022/01/27/pedofil/",
    "source": "Силовые структуры",
    "date": "27.01.2022 00:01:00"
  },
  {
    "title": "Бритни Спирс станцевала в бикини на камеру и смутила фанатов текстом под видео",
    "url": "https://lenta.ru/news/2022/01/28/alternatives/",
    "source": "Экономика",
    "date": "28.01.2022 23:58:00"
  },
  {
    "title": "Зеленский назвал неправильным и безрезультативным предложение Лаврова встречаться в Сочи",
    "url": "https://yandex.ru/news/story/Zelenskij_nazval_nepravilnym_i_bezrezultativnym_predlozhenie_Lavrova_vstrechatsya_vSochi--0d6952c5e6ef5ea6d522e31a773ab05f?lang=ru&rubric=politics&fan=1&stid=9OBHxT0M5dt2NWBkuOi1&t=1643414680&tt=true&persistent_id=178281930",
    "source": "Lenta.ru",
    "date": "28.01.2022 17:53:47"
  },
  {
    "title": "Лавров заявил об отсутствии у Киева контроля над огромной частью своих военных",
    "url": "https://yandex.ru/news/story/VPeterburge_arestovali_glavvracha_medcentra_gde_troe_pacientov_pogibli_posle_gastroskopii--7b56f35575a23e5408250013e0d72f22?lang=ru&rubric=incident&fan=1&stid=o5j_s9OhMpCpW7q9uRkJ&t=1643414680&tt=true&persistent_id=178279956",
    "source": "Lenta.ru",
    "date": "28.01.2022 19:38:09"
  }
]
```

##### [Yandex-Новости](https://yandex.ru/news/) (example) function overview:

```python
def get_ya_news():
    """Parses news from ya.ru."""

    sources_xpath = '//span[contains(@class, "news-story__subtitle-text")]/text()'
    titles_xpath = '//a[contains(@class, "mg-card__link")]/text()'
    dates_xpath = '//meta[contains(@property, "article:published_time")]/@content'
    links_xpath = '//a[contains(@class, "mg-card__link")]/@href'
    data = parse_news(YA_URL, sources_xpath, titles_xpath, dates_xpath, links_xpath)
    return data
```

