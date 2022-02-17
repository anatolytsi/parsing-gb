# Lesson 8. Working with data

### Collect subscribers and subscription data of random n users from [instagram](https://www.instagram.com/) using [Scrapy](https://scrapy.org/) and save data to DB.

##### Run script:

To parse instagram.com run with the corresponding profiles, e.g., "
kaenmuenchen" `scrapy crawl profiles -a profiles=kaenmuenchen,odessa_feinkost`

###### Collected data example:

Followers:

```json
[
  {
    "_id": {
      "$oid": "620b9b12f3e1f0daf1a82096"
    },
    "pk": 3512408798,
    "username": "luisaleisering",
    "full_name": "𝑳𝑼𝑰𝑺𝑨",
    "photo": [
      {
        "url": "https://scontent-muc2-1.cdninstagram.com/v/t51.2885-19/s150x150/150611246_1094687140997376_4618113277217166521_n.jpg?_nc_ht=scontent-muc2-1.cdninstagram.com&_nc_cat=100&_nc_ohc=RzBSvs5DkDYAX-lxkYx&edm=APQMUHMBAAAA&ccb=7-4&oh=00_AT_j2rJNFn1zVBtPFfluVj5ZzrP4-rQyp77BOtSzEPcayA&oe=62132F18&_nc_sid=e5d0a6",
        "path": "profiles/luisaleisering.jpg",
        "checksum": "01e6941404baaa68a36de93bc833e8a5",
        "status": "downloaded"
      }
    ],
    "is_private": true
  },
  {
    "_id": {
      "$oid": "620b9b13f3e1f0daf1a82099"
    },
    "pk": 1149349485,
    "username": "loverssinnersfriends",
    "photo": [
      {
        "url": "https://scontent-muc2-1.cdninstagram.com/v/t51.2885-19/s150x150/210174320_366679994821430_7477939550756790867_n.jpg?_nc_ht=scontent-muc2-1.cdninstagram.com&_nc_cat=102&_nc_ohc=vAvVxPFvQDcAX8RImBe&edm=APQMUHMBAAAA&ccb=7-4&oh=00_AT-NoFZuiURe50ZkEZUsJNzsAS4mDzUIfSdU49vywWGC4w&oe=62130970&_nc_sid=e5d0a6",
        "path": "profiles/loverssinnersfriends.jpg",
        "checksum": "85ac56d57f136486a099d71363c5ca6e",
        "status": "downloaded"
      }
    ],
    "is_private": true
  }
]
```

Following:

```json
[
  {
    "_id": {
      "$oid": "620b9b0bf3e1f0daf1a8206f"
    },
    "pk": 2305906288,
    "username": "voglferdinand",
    "full_name": "Ferdinand Vogl",
    "photo": [
      {
        "url": "https://scontent-muc2-1.cdninstagram.com/v/t51.2885-19/81206610_452285392114232_5093972268371935232_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-muc2-1.cdninstagram.com&_nc_cat=108&_nc_ohc=051l8pbAwxoAX8pbebI&edm=ALB854YBAAAA&ccb=7-4&oh=00_AT9Cv4aO5ZtwgwqOTVwppRIquNLIkVvME3k_WllSB2YV5A&oe=62127C6D&_nc_sid=04cb80",
        "path": "profiles/voglferdinand.jpg",
        "checksum": "43d1dc628de197de446302a5683e0516",
        "status": "downloaded"
      }
    ],
    "is_private": false
  },
  {
    "_id": {
      "$oid": "620b9b0bf3e1f0daf1a82072"
    },
    "pk": 3597096480,
    "username": "konstantin.mantzaris",
    "full_name": "Konstantin Müller",
    "photo": [
      {
        "url": "https://scontent-muc2-1.cdninstagram.com/v/t51.2885-19/s150x150/105951818_1000965537005421_2605273609129633908_n.jpg?_nc_ht=scontent-muc2-1.cdninstagram.com&_nc_cat=109&_nc_ohc=N4E0dNAQeNgAX_3zeiH&edm=ALB854YBAAAA&ccb=7-4&oh=00_AT-DODdbxPMNaZYdL2YZUsJT5sTh4G7zw2lPsfxDsieVww&oe=6211BB9B&_nc_sid=04cb80",
        "path": "profiles/konstantin.mantzaris.jpg",
        "checksum": "779510f1c78e41474f503cd8ecc13c94",
        "status": "downloaded"
      }
    ],
    "is_private": false
  },
  {
    "_id": {
      "$oid": "620b9b0cf3e1f0daf1a82075"
    },
    "pk": 11123248093,
    "username": "isabella_aus_werdenfels",
    "full_name": "Isabella",
    "photo": [
      {
        "url": "https://scontent-muc2-1.cdninstagram.com/v/t51.2885-19/s150x150/56498747_372822846685146_722723866408910848_n.jpg?_nc_ht=scontent-muc2-1.cdninstagram.com&_nc_cat=106&_nc_ohc=h5NQ9cYE8ncAX8yGS9j&edm=ALB854YBAAAA&ccb=7-4&oh=00_AT-d1qD_xIhGNg1i90kkUAFgB9Vb99RUTDiEEsic09l4Lg&oe=6211F9A8&_nc_sid=04cb80",
        "path": "profiles/isabella_aus_werdenfels.jpg",
        "checksum": "f14ebde031e54b5cb2dd74e5017f2a6d",
        "status": "downloaded"
      }
    ],
    "is_private": false
  }
]
```
