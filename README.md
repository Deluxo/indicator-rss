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

##What's next?
The next step in this project would be to implement smarter fetching, i.e. hide already read items from the list. Or do not store them altogether.
If you have a spare time to contribute, please do.

I'm also thinking about rewriting the structure of the source code (keep the functional bits). The current version is too linear and has very little freedom to expand already.