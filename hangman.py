print("Let's play Hangman!")
print("-----")

playing = True

while playing == True:

    for lives in range(6):
        print("Lives left: " + str(6 - lives))
