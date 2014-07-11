#RSS indicator for *Ubuntu Linux* (and it's derivatives)

###What it does

Shows an indicator with all your favorite RSS feeds.

###How does it do?

It uses feedparser to mangle with the feeds, and pickle to save them for later accessing.

![Alt text](1.png?raw=true "ScreenShot")
![Alt text](2.png?raw=true "ScreenShot")
![Alt text](4.png?raw=true "ScreenShot")
---
###What you will need###
- Python.
- Pip (python module installer).
- Coffee.
- Free time.

###How to setup it up:

In terminal, intall feedparser python module with:
```bash
sudo pip install feedparser
```

To launch it, *cd* to app's root directory where indicator.py is located and:
```bash
python indicator.py
```

To customize the rss sources, edit the *feeds/feeds.txt*