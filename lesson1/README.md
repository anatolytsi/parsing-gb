# Lesson 1. Fundamentals of client-server interactions. API Parsing
### Task 1.
Read the GitHub API documentation, figure out how to get user's list of repositories, and save it as JSON.

##### Function get_user_repos:

```python
def get_user_repos(username: str) -> list:
    """Gets GitHub users list of
    repositories and their urls.

    :param username: GitHub user username.
    :return: list of objects with repos name and url.
    """
    response = requests.get(f'{GIT_URL}/{username}/{GIT_REPOS_RES}')
    response_dict = response.json()
    return [{'name': repo['full_name'], 'url': repo['html_url']} for repo in response_dict]
```

##### Getting anatolytsi's repos:
```json
[
  {
    "name": "anatolytsi/adpp-gb",
    "url": "https://github.com/anatolytsi/adpp-gb"
  },
  {
    "name": "anatolytsi/advanced_js_gb",
    "url": "https://github.com/anatolytsi/advanced_js_gb"
  },
  {
    "name": "anatolytsi/anatolytsi",
    "url": "https://github.com/anatolytsi/anatolytsi"
  },
  {
    "name": "anatolytsi/anatolytsi.github.io",
    "url": "https://github.com/anatolytsi/anatolytsi.github.io"
  },
  {
    "name": "anatolytsi/basic_course_django_gb",
    "url": "https://github.com/anatolytsi/basic_course_django_gb"
  },
  {
    "name": "anatolytsi/basic_course_js_gb",
    "url": "https://github.com/anatolytsi/basic_course_js_gb"
  },
  {
    "name": "anatolytsi/CarRGB_v1",
    "url": "https://github.com/anatolytsi/CarRGB_v1"
  },
  {
    "name": "anatolytsi/cs-apps-gb",
    "url": "https://github.com/anatolytsi/cs-apps-gb"
  },
  {
    "name": "anatolytsi/databases_geekbrains",
    "url": "https://github.com/anatolytsi/databases_geekbrains"
  },
  {
    "name": "anatolytsi/db-pyqt-gb",
    "url": "https://github.com/anatolytsi/db-pyqt-gb"
  },
  {
    "name": "anatolytsi/django-dynamic-formset",
    "url": "https://github.com/anatolytsi/django-dynamic-formset"
  },
  {
    "name": "anatolytsi/django_opt_tools_gb",
    "url": "https://github.com/anatolytsi/django_opt_tools_gb"
  },
  {
    "name": "anatolytsi/drf-gb",
    "url": "https://github.com/anatolytsi/drf-gb"
  },
  {
    "name": "anatolytsi/parsing-gb",
    "url": "https://github.com/anatolytsi/parsing-gb"
  },
  {
    "name": "anatolytsi/python_algos_gb",
    "url": "https://github.com/anatolytsi/python_algos_gb"
  },
  {
    "name": "anatolytsi/python_basics_homeworks",
    "url": "https://github.com/anatolytsi/python_basics_homeworks"
  },
  {
    "name": "anatolytsi/qpc",
    "url": "https://github.com/anatolytsi/qpc"
  },
  {
    "name": "anatolytsi/rpi-python-hvac",
    "url": "https://github.com/anatolytsi/rpi-python-hvac"
  },
  {
    "name": "anatolytsi/rpi-react-hvac",
    "url": "https://github.com/anatolytsi/rpi-react-hvac"
  },
  {
    "name": "anatolytsi/rpi-wot-hvac",
    "url": "https://github.com/anatolytsi/rpi-wot-hvac"
  }
]
```

### Task 2
Check out list of open APIs, find the one that requires auth. Make requests with auth and save responses to JSON.

##### YouTube API was selected. Function get_video_data:
```python
def get_video_data(video_url: str) -> dict:
    """Gets data about a
    YouTube video via its URL.

    :param video_url: YouTube video URL.
    :return: YouTube video data dict.
    """
    match = re.search(r'watch\?v=(.+)', video_url)
    vid_id = match.group(1)
    params = {**PARAMS, 'id': vid_id}
    response = requests.get(f'{YT_URL}/{YT_VIDEOS_RES}', params=params)
    return response.json()
```

##### Getting data about a famous YouTube video:
```json
{
  "kind": "youtube#videoListResponse",
  "etag": "fLWYfHmsN6uko9qKFrlNV3DLvwY",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "52cfoV3owmL3wVn1mDXuysNeVMI",
      "id": "dQw4w9WgXcQ",
      "snippet": {
        "publishedAt": "2009-10-25T06:57:33Z",
        "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
        "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
        "description": "The official video for \u201cNever Gonna Give You Up\u201d by Rick Astley\n \n\u201cNever Gonna Give You Up\u201d was a global smash on its release in July 1987, topping the charts in 25 countries including Rick\u2019s native UK and the US Billboard Hot 100.  It also won the Brit Award for Best single in 1988. Stock Aitken and Waterman wrote and produced the track which was the lead-off single and lead track from Rick\u2019s debut LP \u201cWhenever You Need Somebody\u201d.  The album was itself a UK number one and would go on to sell over 15 million copies worldwide.\n\nThe legendary video was directed by Simon West \u2013 who later went on to make Hollywood blockbusters such as Con Air, Lara Croft \u2013 Tomb Raider and The Expendables 2.  The video passed the 1bn YouTube views milestone on 28 July 2021.\n\nSubscribe to the official Rick Astley YouTube channel: https://RickAstley.lnk.to/YTSubID\n\nFollow Rick Astley:\nFacebook: https://RickAstley.lnk.to/FBFollowID \nTwitter: https://RickAstley.lnk.to/TwitterID \nInstagram: https://RickAstley.lnk.to/InstagramID \nWebsite: https://RickAstley.lnk.to/storeID \nTikTok: https://RickAstley.lnk.to/TikTokID\n\nListen to Rick Astley:\nSpotify: https://RickAstley.lnk.to/SpotifyID \nApple Music: https://RickAstley.lnk.to/AppleMusicID \nAmazon Music: https://RickAstley.lnk.to/AmazonMusicID \nDeezer: https://RickAstley.lnk.to/DeezerID \n\nLyrics:\nWe\u2019re no strangers to love\nYou know the rules and so do I\nA full commitment\u2019s what I\u2019m thinking of\nYou wouldn\u2019t get this from any other guy\n\nI just wanna tell you how I\u2019m feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWe\u2019ve known each other for so long\nYour heart\u2019s been aching but you\u2019re too shy to say it\nInside we both know what\u2019s been going on\nWe know the game and we\u2019re gonna play it\n\nAnd if you ask me how I\u2019m feeling\nDon\u2019t tell me you\u2019re too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\n#RickAstley #NeverGonnaGiveYouUp #WheneverYouNeedSomebody #OfficialMusicVideo",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "Rick Astley",
        "tags": [
          "rick astley",
          "Never Gonna Give You Up",
          "nggyu",
          "never gonna give you up lyrics",
          "rick rolled",
          "the boys soundtrack",
          "the boys amazon prime",
          "Never gonna give you up the boys",
          "official",
          "Rick Roll",
          "music video",
          "Rick Astley album",
          "rick astley official",
          "together forever",
          "Whenever You Need Somebody",
          "rickrolled",
          "WRECK-IT RALPH 2",
          "Fortnite song",
          "Fortnite event",
          "Fortnite dance",
          "fortnite never gonna give you up",
          "rick astley never gonna give you up",
          "rick astley never gonna give you up lyrics"
        ],
        "categoryId": "10",
        "liveBroadcastContent": "none",
        "defaultLanguage": "en",
        "localized": {
          "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
          "description": "The official video for \u201cNever Gonna Give You Up\u201d by Rick Astley\n \n\u201cNever Gonna Give You Up\u201d was a global smash on its release in July 1987, topping the charts in 25 countries including Rick\u2019s native UK and the US Billboard Hot 100.  It also won the Brit Award for Best single in 1988. Stock Aitken and Waterman wrote and produced the track which was the lead-off single and lead track from Rick\u2019s debut LP \u201cWhenever You Need Somebody\u201d.  The album was itself a UK number one and would go on to sell over 15 million copies worldwide.\n\nThe legendary video was directed by Simon West \u2013 who later went on to make Hollywood blockbusters such as Con Air, Lara Croft \u2013 Tomb Raider and The Expendables 2.  The video passed the 1bn YouTube views milestone on 28 July 2021.\n\nSubscribe to the official Rick Astley YouTube channel: https://RickAstley.lnk.to/YTSubID\n\nFollow Rick Astley:\nFacebook: https://RickAstley.lnk.to/FBFollowID \nTwitter: https://RickAstley.lnk.to/TwitterID \nInstagram: https://RickAstley.lnk.to/InstagramID \nWebsite: https://RickAstley.lnk.to/storeID \nTikTok: https://RickAstley.lnk.to/TikTokID\n\nListen to Rick Astley:\nSpotify: https://RickAstley.lnk.to/SpotifyID \nApple Music: https://RickAstley.lnk.to/AppleMusicID \nAmazon Music: https://RickAstley.lnk.to/AmazonMusicID \nDeezer: https://RickAstley.lnk.to/DeezerID \n\nLyrics:\nWe\u2019re no strangers to love\nYou know the rules and so do I\nA full commitment\u2019s what I\u2019m thinking of\nYou wouldn\u2019t get this from any other guy\n\nI just wanna tell you how I\u2019m feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWe\u2019ve known each other for so long\nYour heart\u2019s been aching but you\u2019re too shy to say it\nInside we both know what\u2019s been going on\nWe know the game and we\u2019re gonna play it\n\nAnd if you ask me how I\u2019m feeling\nDon\u2019t tell me you\u2019re too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\n#RickAstley #NeverGonnaGiveYouUp #WheneverYouNeedSomebody #OfficialMusicVideo"
        },
        "defaultAudioLanguage": "en"
      },
      "contentDetails": {
        "duration": "PT3M33S",
        "dimension": "2d",
        "definition": "hd",
        "caption": "false",
        "licensedContent": false,
        "contentRating": {},
        "projection": "rectangular"
      },
      "status": {
        "uploadStatus": "processed",
        "privacyStatus": "public",
        "license": "youtube",
        "embeddable": true,
        "publicStatsViewable": true,
        "madeForKids": false
      },
      "statistics": {
        "viewCount": "1134337825",
        "likeCount": "13205157",
        "favoriteCount": "0",
        "commentCount": "2050558"
      }
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}
```
