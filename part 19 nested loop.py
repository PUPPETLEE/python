#for x in range(4):
#    for y in range(4):
#        print(f'({x},{y})')

numbers =[5,2,5,2,2]

for x in numbers:
    output = ''
    for y in range(x):
        output+='*'
    print(output)
