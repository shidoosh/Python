import pprint

message = '''it was a bright cold day in April, and the clocls were striking thirteen.''' # triple quote ''' to escape all characters
count = {} # empty dictionary 
for character in message.upper():
    count.setdefault(character, 0) # if charcter hasn't been counted yet, put in dictionary and set to 0
    count[character] = count[character]+1 # add one to the value in the (character, count) pair

message_text = pprint.pformat(count)
print(message_text)
    
