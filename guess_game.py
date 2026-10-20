secret = 10
guess = int(input("Guess the secret number: "))
while guess != secret:
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    guess = int(input("Guess the secret number: "))
print("Correct!")