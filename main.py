# importing modules
import random
import hangman_art
import hangman_word

# variables

end_of_game = False
display = []
chosen_word = random.choice(hangman_word.word_list)
logo = hangman_art.logo
stages = hangman_art.stages
len_of_word = len(chosen_word)
# lives
lives = 6
# extra feature optional
incorrect_guess = []
## hint_number = 2

# Test code
# print(f"chosen word is {chosen_word}")

# print logo of game
print(logo)

# display word blanks space

for pos in chosen_word:
    display += "_"

# main code
while not end_of_game:
    guess = input("\nguess a letter\n : ").lower()
    # checking for repeating correct guess
    if guess in display:
        print("hey! you have already guessed that letter.")
        # check with every letter
    else:
        for i in range(len_of_word):
            if chosen_word[i] == guess:
                display[i] = guess
        # user exprience
        if guess in chosen_word:
            print("\nwhoooooho you are winning")
    # user experience
    if guess in incorrect_guess:
        print("\nHey! you'r repeating your mistakes.")
        print("so, I'm not taking your life!")
        
    else:
        # FOR WRONG CASE LOOSE LIFE
        if guess not in chosen_word:
            lives -= 1 # taking lives
            # printing hangman art
            print(stages[lives])
            # puttin in incorrect guess in list
            incorrect_guess.append(guess)
            # user exprience
            print(f"Oopps! '{guess}' not in word.")
            # losing condition
            if lives == 0:
                end_of_game = True
                print("\nyou loose!")
                print(f"\nyou dummy word was... \n: '{chosen_word}'")
#     # if len(incorrect_guess)>=3 and hint_number >0:
#     #         print(f"you have '{hint_number}' hint left.")
#     #         want_hint = input("Want a little hint ? yes or no : ").lower()
#     #         if want_hint[0] == 'y':
#     #             print(f"your little help is {random.choice(chosen_word)} ")
#     #         hint_number -= 1

    # conditin of winning
    if "_" not in display:
        end_of_game = True
        print("you won!!")
    
    
    print(f"{' '.join(display)}")

# print(f"\nall the correct guess are :{','.join(correct_guess)}")
# print(f"\nall the incorrect guess are :{','.join(incorrect_guess)}")