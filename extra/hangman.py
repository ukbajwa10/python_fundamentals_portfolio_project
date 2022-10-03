import random
hangman_graphics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


hangman_graphics.reverse()


# copy your arrays in here, then sort them by shortest to longest. calc the length of each list and divide it into sections.
# the shorter section will be a list of integers from 0 - x
# the longer section will be from x - 100. using random choice and range, randomly pick a value from either the shorter section for ez mode, longer section for hard mode
# for normal mode just ignore this logic

animals = ["Aardvark", "Albatross", "Alligator", "Alpaca", "Ant", "Anteater", "Antelope", "Ape", "Armadillo", "Donkey", "Baboon", "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee", "Bison", "Boar", "Buffalo", "Butterfly", "Camel", "Capybara", "Caribou", "Cat", "Caterpillar", "Cheetah", "Chicken", "Chimpanzee", "Chinchilla", "Clam", "Cobra", "Cockroach", "Cod", "Coyote", "Crab", "Crane", "Crocodile", "Crow", "Deer", "Dinosaur", "Dog", "Dogfish", "Dolphin", "Dove", "Dragonfly", "Duck", "Eagle", "Eel", "Eland", "Elephant", "Elk", "Emu", "Falcon", "Ferret", "Finch", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Gazelle", "Gerbil", "Giraffe", "Gnat", "Goat", "Goldfish", "Goose", "Gorilla", "Grasshopper", "Gull", "Hamster", "Hare", "Hawk", "Hedgehog", "Heron", "Herring", "Hippopotamus", "Hornet", "Horse", "Human", "Hummingbird", "Hyena", "Ibex", "Ibis", "Jackal", "Jaguar", "Jay", "Jellyfish", "Kangaroo", "Koala", "Kookabura", "Lemur", "Leopard", "Lion", "Llama", "Lobster", "Locust", "Magpie",
           "Mallard", "Manatee", "Mandrill", "Mantis", "Meerkat", "Mink", "Mole", "Mongoose", "Monkey", "Moose", "Mosquito", "Mouse", "Mule", "Narwhal", "Newt", "Nightingale", "Octopus", "Okapi", "Opossum", "Oryx", "Ostrich", "Otter", "Owl", "Oyster", "Panther", "Parrot", "Partridge", "Peafowl", "Pelican", "Penguin", "Pheasant", "Pig", "Pigeon", "Pony", "Porcupine", "Porpoise", "Quail", "Rabbit", "Raccoon", "Rail", "Ram", "Rat", "Raven", "Redpanda", "Reindeer", "Rhinoceros", "Rook", "Salamander", "Salmon", "Sardine", "Scorpion", "Seahorse", "Seal", "Shark", "Sheep", "Skunk", "Snail", "Snake", "Sparrow", "Spider", "Squid", "Squirrel", "Starling", "Stingray", "Stork", "Swallow", "Swan", "Termite", "Tiger", "Toad", "Trout", "Turkey", "Turtle", "Viper", "Vulture", "Wallaby", "Walrus", "Wasp", "Weasel", "Whale", "Wildcat", "Wolf", "Wolverine", "Wombat", "Woodpecker", "Worm", "Yak", "Zebra"]

usa_states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
              "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

food = ["Burgers", "Pasta", "Pizza",
        "French Fries", "Chicken Wings", "Spaghetti"]


def Sorting(list):
    sorted_list = sorted(list, key=len)
    return sorted_list


animals_sorted = Sorting(animals)
states_sorted = Sorting(usa_states)
food_sorted = Sorting(food)

print(len(animals))
# print(len(usa_states)) = 55
# print(len(food)) = 6

game_word_index_easy = random.randint(0, 112)

game_word_index_hard = random.randint(113, 187)

print(animals_sorted[game_word_index_easy])
print(animals_sorted[game_word_index_hard])
print(animals_sorted[160])
