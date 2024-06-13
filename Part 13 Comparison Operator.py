'''
temperature = 30

if temperature >=30:
    print("It's a hot day")
else:
    print("it not a hot day")

    if len(name)<3:
    print('name must be at least 3 characters long')
elif len(name)>=50:
    print('name can be more than 50 characters long')
else:
    print('name looks good!')
'''
name = input("Enter your name: ")
if len(name)<3:
    print('name must be at least 3 characters long')
elif len(name)>=50:
    print("name can't be more than 50 characters long")
else:
    print("name looks good")


