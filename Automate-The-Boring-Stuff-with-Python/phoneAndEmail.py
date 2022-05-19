#! python3

import re, pyperclip 


#TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
### 710-555-5555, 555-5555, (415) 555-0000, 555-0000 ext 12345, ext.12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?         # area code (optional)
(\s|-)                           # first separator
\d\d\d                           # first 3 digits
-                                # separator
\d\d\d\d                         # last 4 digits
(((ext(\.)?\s)|x) (\d{2,5}))?    # extension (optional)
)
''', re.VERBOSE)


#TODO: Create a regex for emails
emailRegex = re.compile(r'''
#some.+_thing@something.com,net,edu

[a-zA-Z0-9.+_]+         # name part
@                       # @ symbol
[a-zA-Z0-9.+_]+         # domain 

''', re.VERBOSE)
#TODO: Get text off clipboard
text = pyperclip.paste()



#TODO: Extract the email/Phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


allPhoneNumbers = []
for i in extractedPhone:
    allPhoneNumbers.append(i[0])




#TODO: Copy the extracter email/phone to the clipboard 

phoneResults = '\n'.join(allPhoneNumbers)
emailResults = '\n'.join(extractedEmail)

pyperclip.copy(phoneResults + emailResults)


