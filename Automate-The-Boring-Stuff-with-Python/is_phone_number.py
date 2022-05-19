def isPhoneNumber(text): #555 - 555 - 5555
    if len(text) != 12:
        return False
    for i in range(0,3):    # area code
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range (4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False


    for i in range (8,12):
        if not text[i].isdecimal():
            return False

    return True


print(isPhoneNumber('555-555-5555'))
print(isPhoneNumber('hi'))


message = 'Call me at 333-33-3333 or 888-88-8888'
print(message)
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12] #slice
    if isPhoneNumber(chunk):
        foundNumber = True
        print('Phone number found: ' + chunk)
if not foundNumber:
    print('No phone numbers found')
