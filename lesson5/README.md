# Lesson 5. Selenium
### Parse emails from mail.ru personal page ([mail.ru](https://mail.ru/)

##### Run script:

A script entry point is file `mailru_emails.py`

##### Functionality:

Script parses emails from [mail.ru](https://mail.ru/), then saves results to a json.

###### Collected data example:
```json
[
  {
    "title": "Tesla Update, Inclusive Design, Block Protocol, HyperCardSimulator, Polypane 8",
    "from": "Sidebar",
    "when": "02.02.2022 10:10:00",
    "body": "Email not displaying properly? View browser version.\nFEBRUARY 2 2022\nIs Tesla’s v11 update… bad design?\nmedium.com\nAfter months of anticipation, Tesla finally released a shiny new UI update for their vehicles.\nUI UX\nCredit: Geek Culture\nInclusive Design\nnngroup.com\nInclusive design describes methodologies to create products that understand and enable people of all backgrounds and abilities.\nInclusivity\nCredit: Nielsen Norman Group\nMaking the web better. With blocks!\njoelonsoftware.com\nYou’ve probably seen web editors based on the idea of blocks.\nNews\nCredit: Joel Spolsky\nHyperCardSimulator\nhypercardsimulator.com\nExplore how the stack-of-cards architecture and intuitiveness of HyperCard might be on the modern web with painting, authoring and scripting tools.\nExperiment UI History\nCredit:\nPolypane 8\npolypane.app\nA better Elements inspector, performance improvements, Chromium 98, forced colors emulation, focus state sync, ARM support, a new debug tool and more.\nCSS News\nCredit: Polypane. The browser for ambitious developers\n  You’re receiving this email because you signed up on sidebar.io. Unsubscribe\nSacha Greif - Kyoto, Japan"
  },
  {
    "title": "30 Maps, Greatest Innovations, Emoji to Scale, Emoji Frequency, Projects of the Year",
    "from": "Sidebar",
    "when": "06.12.2021 10:15:00",
    "body": "Email not displaying properly? View browser version.\nDECEMBER 6 2021\n30 days and as many maps\nobservablehq.com\nEmbarking on this challenge felt like an opportunity to finish a few open projects, to try a few ideas, and to showcase a part of my usual toolbox.\nData Visualization\nCredit: Visions carto\nThe 100 greatest innovations of 2021\npopsci.com\nPopular Science’s 34th annual Best of What’s of New awards include life-saving vaccines—and 99 other technologies shaping our future.\nNews\nCredit: Popular Science\nEmoji to Scale\njavier.xyz\nYour favorite emojis. To scale (more or less).\nEmojis Humor\nCredit: Javier Bórquez\nEmoji Frequency\nhome.unicode.org\n'Unicode Unwrapped' just dropped and the most used emojis of the year are now visualized on this Frequency page.\nEmojis\nCredit: The Unicode Consortium\n2021: Projects of the Year Sponsored\nreadymag.com\nGet inspired by websites created with Readymag in 2021 and vote for the best in Typography, Navigation, Visual Storytelling and First Page.\nInspiration\nCredit: Readymag\n  You’re receiving this email because you signed up on sidebar.io. Unsubscribe\nSacha Greif - Kyoto, Japan"
  }
]
```
