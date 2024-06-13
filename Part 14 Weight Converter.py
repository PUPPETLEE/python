weight  = input('Weight: ')
answer =input("(L)bs or (K)g: ")
if answer.lower()==('l'):
    converter =int(weight)*0.45
    print(f"Your are {round(converter,2)} kilo")
elif answer.lower()==('k'):
    converter = int(weight) / 0.45
    print(f"Your are {round(converter,2)} pounds")


