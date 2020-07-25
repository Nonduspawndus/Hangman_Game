def play_chance(word, correct_guess, wrong_guess):
    s = ""
    h = ""
    hang = "HANGMAN"
    chances_left = len(hang) - len(wrong_guess)
    for i in range(len(word)):
        if word[i] == " ":
            s += "/"
        elif word[i] in correct_guess:
            s += " " + word[i] + " "
        else:
            s += " _ "
    h = "X " * (len(wrong_guess))
    for i in hang[len(wrong_guess):]:
        h += i + " "
    winninig_condition = "_" not in s
    print("\n" + h + "\t Chances left: " + str(chances_left) + "\n")
    print(s + "\n")
    return chances_left,  winninig_condition
# play_chance("JUMPING MONKEY", ["O", "I", "M", "Y"], ["A", "B", "C", "F"])

print("Welcome to Hangman.\nRules:  \nYou will get a word or a phrase or a movie to guess. \nYou will get 7 tries to guess it. \nLet's start!")
word = "LA CASA DE PAPEL"
correct_guess = []
wrong_guess = []
chances_left, winninig_condition = play_chance(word, correct_guess, wrong_guess)
while chances_left>0 and winninig_condition == False:
    guess = input(">").upper()
    if guess in word:
        correct_guess.append(guess)
    elif guess not in word:
        wrong_guess.append(guess)
    else:
        print("Invalid Input. Please enter again.")
    chances_left, winninig_condition = play_chance(word, correct_guess, wrong_guess)









# s = ''
# for word in movie.split():
#     s += len(word) * ' _ ' + '/'
######################
