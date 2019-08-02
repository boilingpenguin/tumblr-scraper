# tumblr-scraper
A simple python script to search Tumblr for posts with a specified tag

## Welcome
This is a super simple (and poorly-written) python script that uses the Tumblr API (https://github.com/tumblr/docs/blob/master/api.md) to search for a specified tag and collate any matching posts. The script will generate a CSV file with up to 100 Tumblr posts that are tagged with the specified term.

## Required Modules:
This script uses the following python modules:
- pytumblr
- datetime
- time
- calendar
- unicodecsv
- unidecode

Make sure that you have all of these installed and updated before running the script to avoid any problems.

## Other Requirements:
### Python API keys
Tumblr requires that API requests for tagged posts include authentication. You'll need to register a Tumblr account and register an application. Once you have your API key, you'll enter that into line 13 of the python script.
For more see: https://www.tumblr.com/docs/en/api/v2#authentication

### Basic working knowledge of python
This script has no fancy GUI, and no interactive entry of search terms. Sorry. I cobbled this whole thing together for my own research project. You'll need to be comfortable opening and editing python scripts in order to set your own search terms, etc.

## How to use: ##
1. Before running, open the file and adjust the variables toward the top of the file. Make sure to enter your Tumblr API Key on line 13.

After the API key, you'll need to set the `tag`, `filter`, `before`, and `outputPath` variables.
- tag - enter your search term here. Phrases separated with spaces work okay.
- filter - choose text, html, or raw. Text will return plain-text results, HTML will include the HTML (what a surprise!) and raw will return exactly what the user inputted (typically either HTML or markdown)
- before - choose to only return posts before a specified timestamp (in seconds past the epoch). (https://www.epochconverter.com/ is a useful converter). You can also just use `calendar.timegm(time.gmtime())` to use the current system time.
- outputPath - specifiy where you'd like the CSV file to be saved to

For example:

`tag = 'female presenting nipples'`

`filter = 'raw'`

`before = 1576616584`

`outputPath = '/Users/boilingpenguin/Desktop/tumblrScrape/'`


2. Run the `tumblrTagScrape.py` python file. 
3. That's it. Just sit back and wait.
