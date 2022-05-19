import requests, sys, webbrowser, bs4
print('Searching...')  #Display text while downloading search result page.  
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])) 
print(sys.argv[1:])
res.raise_for_status()

# Retrieve top search result links. 
# Get only the text from the downloaded html file
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Open a browser tab for each result, the element looks like this when search the term "boring stuff": <a class="package-snippet" href="/project/boring/">
# Select the elements that belong to package-snippet class (these are the search results)
linkElems = soup.select('.package-snippet')


# min returns the smaller of the two. So, get five results if there is more than five, or all of the results if there are less than 5 results 
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # join the href to the base url
    # "<a class="package-snippet" href="/project/boring/"
    urlToOpen = 'http://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
