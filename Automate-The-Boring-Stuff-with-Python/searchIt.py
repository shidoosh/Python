import webbrowser, sys

if len(sys.argv) > 1:
    searchItems = ' '.join(sys.argv[1:])

else:
    print('Please enter what you are looking for')
    searchItems = input()


webbrowser.open('https://www.google.com/search?q=' + searchItems)
