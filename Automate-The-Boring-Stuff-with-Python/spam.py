spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        # this causes 3 to never be printed since continue interrupts loop to start over
        continue
    print ('spam is ' + str(spam))
