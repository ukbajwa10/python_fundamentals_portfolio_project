import random
from extra.hangman import hangman_graphics, animals_sorted, states_sorted, food_sorted


while True:
    print("\nWelcome to HANGMAN!")
    print(hangman_graphics[0])
    print("H A N G M A N")
    print("_ _ _ _ _ _ _")

    print("\n1) Animals")
    print("2) States and Provinces of the U.S.A.")
    print("3) Food Dishes")

    topic_choice = input("Select a game topic(1, 2, or 3): ")
    print("\n1) Easy. In Easy mode, shorter words are in the selection pool.")
    print("2) Normal. In Normal mode, there is no restriction on the word selection.")
    print("3) Hard. In Hard mode, longer words are in the selection pool and there is a penalty for guessing the same letter more than once.")
    game_difficulty = input("Select a game mode(1, 2, or 3): ")

    if topic_choice == "1" and game_difficulty == "1":
        print("You selected 'Animals' (EASY)!")
        game_word_index = random.randint(0, 112)
        game_word = animals_sorted[game_word_index].lower()
    elif topic_choice == "1" and game_difficulty == "2":
        print("You selected 'Animals' (NORMAL)!")
        game_word = random.choice(animals_sorted).lower()
    elif topic_choice == "1" and game_difficulty == "3":
        print("You selected 'Animals' (HARD)!")
        game_word_index = random.randint(113, 187)
        game_word = animals_sorted[game_word_index].lower()
    elif topic_choice == "2" and game_difficulty == "1":
        print(
            "You selected 'States and Provinces of the United States of America' (EASY)!")
        game_word_index = random.randint(0, 34)
        game_word = states_sorted[game_word_index].lower()
    elif topic_choice == "2" and game_difficulty == "2":
        print(
            "You selected 'States and Provinces of the United States of America' (NORMAL)!")
        game_word = random.choice(states_sorted).lower()
    elif topic_choice == "2" and game_difficulty == "3":
        print(
            "You selected 'States and Provinces of the United States of America' (HARD)!")
        game_word_index = random.randint(35, 54)
        game_word = states_sorted[game_word_index].lower()
    elif topic_choice == "3" and game_difficulty == "1":
        print("You selected 'Food Dishes' (EASY)!")
        game_word_index = random.randint(0, 14)
        game_word = food_sorted[game_word_index].lower()
    elif topic_choice == "3" and game_difficulty == "2":
        print("You selected 'Food Dishes' (NORMAL)!")
        game_word = random.choice(food_sorted).lower()
    elif topic_choice == "3" and game_difficulty == "3":
        print("You selected 'Food Dishes' (HARD)!")
        game_word_index = random.randint(15, 26)
        game_word = food_sorted[game_word_index].lower()

    # Reference hangman.py for number of lives; Number of lives corresponds to each graphic, 6 is the highest and player dies at 0
    number_of_lives = 6
    game_word_list = list(game_word)
    number_of_blanks = []
    guessed_letters = []

    # Populate the blanks list with blanks equal to the length of the word
    for x in game_word:
        number_of_blanks.append("_")

    # If there are spaces in the word, auto-insert those into the solution so the player does not have to guess spaces
    if " " in game_word_list:
        space_indices = [i for i, x in enumerate(
            game_word_list) if x == " "]
        for space_index in space_indices:
            number_of_blanks.pop(space_index)
            number_of_blanks.insert(space_index, " ")

    print(hangman_graphics[number_of_lives])
    print(*number_of_blanks, sep=" ")

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
            print("\nLetters guessed so far: ", *guessed_letters, sep=' ')

        elif letter_guess in guessed_letters:
            if game_difficulty == "3":
                print("You already tried that letter! You lose a life.")
                number_of_lives -= 1
                print(hangman_graphics[number_of_lives])

            else:
                print(
                "\nYou already tried that, please pay attention to the 'letters guessed so far'.")

        else:
            guessed_letters.append(letter_guess)
            print("Bad guess, you lost a life!")
            number_of_lives -= 1
            print(hangman_graphics[number_of_lives])
            print("\nLetters guessed so far: ", *guessed_letters, sep=' ')
            print(*number_of_blanks, sep=" ")

    if number_of_lives == 0:
        print(f"You lose!\nThe word was {game_word.capitalize()}")
        keep_playing = input("Would you like to play again? 'Yes or No' ")
        if keep_playing.lower() == "no":
            exit()
        else:
            pass
    else:
        print("You win!")
        keep_playing = input("Would you like to play again? 'Yes or No' ")
        if keep_playing.lower() == "no":
            exit()
        else:
            pass
