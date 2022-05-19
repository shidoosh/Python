import re # regex module 



message = 'Call me at 333-333-3333 or 888-888-8888'

#re.compile takes regex arg
#usually takes raw strings
#\d matches digits
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')

#re has search method, will search the string passed and
#find first occurence of the match
#returns a match object
#matchObject = phoneNumRegex.search(message)

#findall() will find all matches, not just first occurence

matchList = phoneNumRegex.findall(message)

#match objects have a group method that tells you the actual text
#print(matchObject.group())

#findall returns list, so no need for group, can just print as is

print(matchList)
