import requests, sys, webbrowser, bs4


print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]), 'html.parser')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
