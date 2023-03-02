import webbrowser
import sys
from pprint import pprint

BASE_URL = 'https://www.google.com/search?q='
CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def create_query():
    
    query = sys.argv[1:]
    
    return str(' '.join(query)) 
    

def create_url():
    if len(sys.argv[1:]) == 0:
        print('Please enter A valid argument')
    else:
        return BASE_URL+create_query()

webbrowser.get(CHROME_PATH).open(create_url())
 

#Add DOSKEY to PATH variable: https://superuser.com/questions/988311/doskey-is-not-recognized-when-using-cmder
 #For windows to set up an alias permenantly (I used the second method): https://superuser.com/questions/1134368/create-permanent-doskey-in-windows-cmd
 