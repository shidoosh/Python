import random

EightBall = ['It is certain.',
         'It is decidedly so.',
         'Without a doubt.',
         'Yes definitely.',
         'You may rely on it',
         'As I see it, yes.',
         'Most likely.',
         'Outlook good.',
         'Yes.',
         'Signs point to yes.',
         'Reply hazy, try again.',
         'Ask again later.',
         'Better not tell you now.',
         'Cannot predict now.',
         'Concentrate and ask again',
         'Don\'t count on it.',
         'My reply is no.',
         'My sources say no.',
         'Outlook not so good.',
         'Very doubtful.']
      

def ask():
    print('...I am a Magic 8 Ball ... Ask me anything and I will tell you your future...')
    input()
    answer = random.randint(0,19)
    print(EightBall[answer])

    yes_or_no = ['Y', 'N']
    while True: 
        print('Do you have another question? (y/n)')
        i = input().upper()
        while i not in yes_or_no:
            print('Please enter \'y\' to ask again or \'n\' to quit.')
            i = input().upper()
        if i == 'Y':
            ask()
        else:
            print('Good Luck.')
            exit()
    
ask()
