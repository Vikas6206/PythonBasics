# i=1;
#
# while i<=5:
#     print('*' * i)
#     i+=1
# print("Done")

guess_number=9
guess_count=0
guess_limit=3

print(f"Guess the correct value in {guess_limit} attempt")
while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count+=1
    if guess == guess_number:
        print("You won !!")
        break
else:
    print("You lose :(")
