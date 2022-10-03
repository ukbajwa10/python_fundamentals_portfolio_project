import random
from extra.hangman import hangman_graphics, animals_sorted, states_sorted, food_sorted

print("1) Animals")
print("2) States of the U.S.A.")
print("3) Food Dishes")

game_word = ""
topic_choice = input("Select a game topic: ")

if topic_choice == "1":
    print("You selected 'Animals'!")
    game_word = random.choice(animals_sorted).lower()
elif topic_choice == "2":
    print("You selected 'States of the United States of America'!")
    game_word = random.choice(states_sorted).lower()
elif topic_choice == "3":
    print("You selected 'Food Dishes'!")
    game_word = random.choice(food_sorted).lower()

# Reference hangman.py for num of lives; Num of lives corresponds to each graphic, 6 is the highest and player dies at 0
number_of_lives = 6
game_word_list = list(game_word)
number_of_blanks = []
guessed_letters = []

# Populate the blanks list with blanks equal to the length of the word
for x in game_word:
    number_of_blanks.append("_")

# If there are spaces in the word, auto-insert those into the solution so the player doesnt have to guess spaces
if " " in game_word_list:
    space_indices = [i for i, x in enumerate(
        game_word_list) if x == " "]
    for space_index in space_indices:
        number_of_blanks.pop(space_index)
        number_of_blanks.insert(space_index, " ")

print(hangman_graphics[number_of_lives])
print(*number_of_blanks, sep=" ")
print(game_word)

while number_of_lives > 0 and "_" in number_of_blanks:
    letter_guess = input("Guess a letter: ").lower()
    if letter_guess in game_word_list:
        guessed_letters.append(letter_guess)
        print("Good guess!")
        letter_indices = [i for i, x in enumerate(
            game_word_list) if x == letter_guess]
        for letter_index in letter_indices:
            number_of_blanks.pop(letter_index)
            number_of_blanks.insert(letter_index, letter_guess)
            game_word_list.pop(letter_index)
            game_word_list.insert(letter_index, "_")
        print(hangman_graphics[number_of_lives])
        print(*number_of_blanks, sep=" ")
        print("")
        print("Letters guessed so far: ", *guessed_letters, sep=' ')
        print("")
    elif letter_guess not in game_word_list:
        guessed_letters.append(letter_guess)
        print("Bad guess, you lost a life!")
        number_of_lives -= 1
        print(hangman_graphics[number_of_lives])
        print("")
        print("Letters guessed so far: ", *guessed_letters, sep=' ')
        print("")
        print(*number_of_blanks, sep=" ")


if number_of_lives == 0:
    print("You lose!")
else:
    print("You win!")
