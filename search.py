import webbrowser
import sys
from pprint import pprint

BASE_URL = 'https://www.google.com/search?q='
CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def create_query():
    
    query = sys.argv[1:]
    return ' '.join(query) 
    

def create_url():
    if len(sys.argv[1:]) == 0:
        print('Please enter A valid argument')
    else:
        return BASE_URL+create_query()

webbrowser.get(CHROME_PATH).open(create_url())
 