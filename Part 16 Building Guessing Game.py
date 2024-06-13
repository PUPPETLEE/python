guess_count = 0
guess_limit = 3
secret_number = 5

while guess_limit>guess_count:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess.__eq__(secret_number ):
        print("You win")
        break
else:
    print("You lose")


