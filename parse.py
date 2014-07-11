import feedparser
import cPickle as pickle
f = open('feeds/feeds.txt','r')
feed_urls_list = f.read().split('\n')
f.close()
for i in range(len(feed_urls_list)):
  feed = feedparser.parse(feed_urls_list[i])
  f =  open("feeds/feed"+str(i)+".p","w")
  pickle.dump(feed,f)
  f.close()
print "Completed."