hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]
num_wrong_guesses_allowed = len(hangman_parts)
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)


stored_name = input("What is your name? ")
print("Hello, {}! It's time to play hangman".format(stored_name))

find_word = "test"

guesses_made = []

errors = 0
while errors < num_wrong_guesses_allowed:
    guess = input("\nEnter a letter: ")
    guesses_made.append(guess)
    print(guesses_made)

    if guess.lower() in find_word:
        print("Good job!")
    else:
        print("Try again. You failed at life.")
        errors = errors + 1
        print("errors = {}".format(errors))
        if errors == num_wrong_guesses_allowed:
            print("Sorry, You've lost")

    draw_hangman(errors)






























