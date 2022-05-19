def eggs(cheese):
    cheese.append('Hello')
    
spam = [1, 2, 3] # spam has a reference to this list
eggs(spam)       # since cheese pointed at same object as spam, spam is now modified "outside" of the scope 
print(spam)
