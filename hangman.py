from random_word import RandomWords

print("Let's play Hangman!")
print("-----")

playing = True

while playing == True:

    for lives in range(6):
        print("Lives left: " + str(6 - lives))
        guess = input("Guess a letter:\n")

        for letter in guess:
            if letter in word:
                print("Correct!")
            else:
                print("Incorrect!")
