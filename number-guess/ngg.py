import random
import time

print("Welcome to the Number Guessing Game!\n\
I'm thinking of a number between 1 and 100.\n")

hs = [[-1, -1], [-1, -1], [-1, -1]]

while True:
    ask1 = input("Want to see high scores? (Y/N) ")
    while ask1.upper() not in ["Y", "N"]:
        print("Invalid.\n")
        ask1 = input("Want to see high scores? (Y/N) ")

    if ask1 in "Yy":
        if all(row[0] == -1 for row in hs):
            print("No games played.")
        else:
            for rowind in range(len(hs)):
                if hs[rowind][0] == -1:
                    continue
                print(["Easy", "Medium", "Hard"][rowind], ": ", hs[rowind][0], " attempts and ", hs[rowind][1], " seconds.", sep = "")

    print("\nPlease select the difficulty level:\n\
1. Easy (10 chances)\n\
2. Medium (5 chances)\n\
3. Hard (3 chances)\n")

    mode = input("=> ")

    while mode not in ["1", "2", "3"]:
        print("Invalid. Re-enter the mode.")
        mode = input("=> ")

    mode = int(mode) - 1

    print("\nSelected difficulty:", ["Easy", "Medium", "Hard"][mode])
    answer = random.randint(1, 100)

    guesses = [10, 5, 3][mode]
    mg = guesses
    win = False

    print("*"*50)
    starttime = time.time()
    
    while guesses:
        guess = input("\nEnter a number to guess: ")
        while guess.isdigit() == False or int(guess) not in range(1, 101):
            print("Invalid. Re-enter the guess.")
            guess = input("Enter a number to guess: ")
        guess = int(guess)

        if guess != answer:
            print("Incorrect! The number is", ("lesser" if guess > answer else "greater"), "than", guess)
            guesses -= 1
        else:
            g = mg-guesses+1
            t = round(time.time() - starttime, 2)
            print("Congratulations! You guessed the correct number in", g, "attempt(s) and", t, "seconds.")
            win = True
            if hs[mode][0] == -1:
                hs[mode] = [g, t]
            else:
                if hs[mode][0] > g:
                    hs[mode][0] = g
                if hs[mode][1] > t:
                    hs[mode][1] = t
            break

    if win == False:
        print("\nYou lose! The correct answer was:", answer)

    ask = input("\nWant to play again? (Y/N) ")
    while ask.upper() not in ["Y", "N"]:
        print("Invalid.\n")
        ask = input("Want to play again? (Y/N) ")

    if ask.upper() == "N":
        break

    print("*"*50, "\n")
