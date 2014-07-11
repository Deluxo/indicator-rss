#!/usr/bin/env python
# Version 1.0
# To do:
#   * Filter read items
#   * Optimise memory usage
#   * Auto refresh
#   * Get the latest feeds date, when updating, update pickled dict only from the date given
#   * Parse fresh feed, remove keys stored in dict, maybe use plain list, replace file for use, rerun the app.

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator
from configobj import ConfigObj
from multiprocessing import Process
import cPickle as pickle
import sys
import os
import webbrowser
import feedparser
import time
import commands

workplace = commands.getoutput('pwd')

if __name__ == "__main__":
	ind = appindicator.Indicator.new ("indicator-rss",workplace+"/icons/i-n.svg",appindicator.IndicatorCategory.APPLICATION_STATUS)
	ind.set_status (appindicator.IndicatorStatus.ACTIVE)
	ind.set_attention_icon(workplace+"/icons/i-a.svg")

def Quit(w):
	sys.exit(0)

def ReadAll(w, main_menu, channel_item):
	main_menu.remove(channel_item)
	SetLastTime()

def ReadEntry(w, link, channel_menu, entry, title, item_number, feed_number):
	webbrowser.open(link)
	channel_menu.remove(entry)
	f = open("feeds/feed"+str(feed_number)+".p","r")
	feed = pickle.load(f)
	f.close()
	del feed["items"][item_number]
	f = open("feeds/feed"+str(feed_number)+".p","w")
	pickle.dump(feed, f)
	f.close()
	feed.clear()
	SetLastTime()


def CheckForRead(feed):
	pass

def Menu():
	f = open('feeds/feeds.txt','r')
	feed_urls_list = f.read().split('\n')
	f.close()
	# Open cached entries
	feed_list = []
	for i in range(len(feed_urls_list)):
		f = open("feeds/feed"+str(i)+".p","r")
		feed = pickle.load(f)
		f.close()
		feed_list.append(feed)
	# create a menu
	main_menu = Gtk.Menu()
	# Channel
	def Seperate(menu):
		separator = Gtk.SeparatorMenuItem()
		menu.append(separator)
		separator.show()
	for i in range(len(feed_list)):
		feed = feed_list[i]
		channel_menu = Gtk.Menu()
		channel_item = Gtk.MenuItem(feed["channel"]["title"])
		channel_item.set_submenu(channel_menu)
		main_menu.append(channel_item)
		channel_item.show()
		# Entries for a Channel
		menu_readall = Gtk.MenuItem("Read all")
		menu_readall.connect("activate", ReadAll, main_menu, channel_item)
		channel_menu.append(menu_readall)
		menu_readall.show()
		Seperate(channel_menu)
		for x in range (len(feed["items"])):
			try:
				print feed["items"][x]["published"]
			except KeyError:
				print "'Published' missing"
			entry = Gtk.MenuItem(feed["items"][x]["title"])
			link = feed["items"][x]["link"]
			title = feed["items"][x]["title"]
			feed_number = i
			item_number = x
			entry.connect("activate", ReadEntry, link, channel_menu, entry, title, item_number, feed_number)
			channel_menu.append(entry)
			entry.show()
		CheckForRead(feed)
		feed.clear()
	# Separator
	Seperate(main_menu)
	# Fetch the news with Parse()
	menu_fetch = Gtk.MenuItem("Fetch")
	main_menu.append(menu_fetch)
	menu_fetch.connect("activate",Parse, ind)
	menu_fetch.show()
	# Quit
	menu_quit = Gtk.MenuItem("Quit")
	main_menu.append(menu_quit)
	menu_quit.connect("activate",Quit)
	menu_quit.show()
	# End stuff
	ind.set_status(appindicator.IndicatorStatus.ACTIVE)
	ind.set_menu(main_menu)

	Gtk.main()

def Update(w, ind):
	os.system('notify-send -i internet-news-reader "RSS" "Feeds updated."')
	ind.set_status(appindicator.IndicatorStatus.ATTENTION)
	Menu()

def Parse(w, ind):
	f = open('feeds/feeds.txt','r')
	feed_urls_list = f.read().split('\n')
	f.close()
	ind.set_status(appindicator.IndicatorStatus.ATTENTION)
	os.system('notify-send -i internet-news-reader "RSS" "Fetching news..."')
	for i in range(len(feed_urls_list)):
		feed = feedparser.parse(feed_urls_list[i])
		f = open("feeds/feed"+str(i)+".p","w")
		pickle.dump(feed,f)
		f.close()
		feed.clear()
	feed.clear()
	Update(w, ind)
	print GetLastTime()

def SetLastTime():
	f = open('feeds/read.txt','w')
	f.write("%.f" % time.time())
	f.close()

def GetLastTime():
	f = open('feeds/read.txt', 'r')
	return f.readline()
	f.close()

Menu()