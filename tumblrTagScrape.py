# Tumblr Tag Scraper
# (C) 2019 Ben Pettis
# www.benpettis.ninja
import pytumblr, datetime
import unicodecsv as csv
from unidecode import unidecode
import calendar
import time

# Enter your Tumblr API key here:

tumblr = pytumblr.TumblrRestClient(
    ''
)

# Set search parameters here: 
#
# Tumblr's API only supports searching for a single tag at a time
# Filter options are text, html, or raw
# Before - only search for posts before this time - in seconds past the epoch
# use calendar.timegm(time.gmtime()) to use the current epoch
tag = ''
filter = 'raw'
before = calendar.timegm(time.gmtime())

#Set output file here:
outputPath = ''


filePath = outputPath + 'TumblrSearch-' + str(before) + '-' + tag + '.csv'
with open(filePath, mode='a') as results_file:
		results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		results_writer.writerow(["timeStamp", "URL", "blogName", "title", "tags", "body"])	


print("Searching Tumblr for 100 posts tagged \'" + tag + "\'")

j = 1

#If you really wanted to, you could increase this number here to increase the number of batches
#Tumblr's API limits you to 20 results at a time, but we can loop through the search multiple times
#BUT I'd be cautious about making this number too big - to avoid running into api call limits

while j < 5:
	#Run the tag search and snag the results
	searchResults = tumblr.tagged(tag, filter=filter, before=before)
	print("Batch " + str(j) + " of 5")
	print(str(len(searchResults)) + " results retreived")
	for i in searchResults:
		blog_name = (i)['blog_name']
		date = (i)['date']

		url = (i)['post_url']
	
		try:
			title = (i)['title']
		except:
			title = "Couldn't Get Title"
		try:
			tags = (i)['tags']
		except:
			tags = "Couldn't Get tags"
		try:
			body = (i)['body']
		except:
			body = "Couldn't Get Post Body"
		with open(filePath, mode='a') as results_file:
			results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
			try:
				results_writer.writerow([date, unidecode(url), blog_name, title, tags, body])
				print("Successfully Wrote Row for post from " + date)
			except:
				print("Error Writing Row")
	#Next we make note of the oldest timestamp	
		oldestTime = (i)['timestamp']
	before = oldestTime
	j = j + 1
print("Finished!")
print("Saved CSV to " + filePath)

