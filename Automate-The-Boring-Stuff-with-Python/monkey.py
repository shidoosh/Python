print('How many monkeys are there?')
numMonkeys = int(input())
for i in range (numMonkeys, 0, -1):
    print(str(i) + ' little monkeys jumping on the bed')
    print('One fell off and bumped his head')
    print('Mama called the doctor and the doctor said')
    if i <= 1:
        print('Put those monkeys right to bed!!!')
    else:
        print('No more monkeys jumping on the bed!')
