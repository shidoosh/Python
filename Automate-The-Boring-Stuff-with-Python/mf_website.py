import urllib.request    

import re



urllib.request.urlretrieve("https://motherfuckingwebsite.com/", "test.txt")
f = open('test.txt','r')
textToChange = f.read()
f.close()


fRegex = re.compile(r'fuck')
sRegex = re.compile(r'shit')

textToChange = fRegex.sub('frick', textToChange)
textToChange = sRegex.sub('shiz', textToChange)


f1 = open('results.txt', 'w')
f1.write(textToChange)

f1.close()
