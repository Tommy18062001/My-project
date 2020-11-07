import random
import time


class Questions:
    # for this class, i am going to create two variable for making our code easy to read, for me
    # i like to use class all the time
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


prompts = ["It has a circle shape and has a really huge impact in our lives insomuch that we say it's indispensable.",
           "The color of the sky."]
secret_word = ["sun", "blue"]

questions = [
    Questions(prompts[0], secret_word[0]),
    Questions(prompts[1], secret_word[1])
]


# this will take a random word from our lists
word = random.choice(secret_word)

# we need to tell our user how long is the word to guess, right?
length = len(word)

name = input("What is your name: ")

print("Welcome " + name + "!!!")
print()

# i don't what does it mean actually, i need to figure this out
time.sleep(2)

print("This is a game called Hangman.\nThe rule is simple: you should guess the word with 3 attempts.\nBest of luck!!!")
print()
time.sleep(2)

print("Test begin now.....")
print()
# got it, it will stop the run during 2 seconds.
time.sleep(2)

count = 0
display = "*" * length

# i created because it will be better for you to guess the word with that. it's like a cue
for question in questions:
    if word in question.answer:
        print(">  " + question.prompt)
        print()
time.sleep(2)


def hangman(count, display, word):
    praise = ["Correct", "That's true", "you are good at guessing huh!!"]

    # this is just for saying that, you have 3 attempts
    limit = 3

    guess = input("This is word: " + display + " Enter your guess: ")
    # i create this because there may be some user that want to break the rule even though they know it.
    if len(guess) == 1:
        # check the user input
        if guess.lower() in word:
            # this is a new things to me ( .find())
            index = word.find(guess)
            # just walk through it slowly and you 'll understand it
            word = word[: index] + "*" + word[index + 1:]
            display = display[: index] + guess + display[index + 1:]

            print(random.choice(praise))

            print()

            print(display)

        else:
            count += 1
            if count == 1:
                print()
                print("wrong input, " + str(limit - count) + " guess remaining")
                print("  ________  \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n"
                      "__|__        \n")

            elif count == 2:
                print()
                print("wrong input, " + str(limit - count) + " guess remaining")
                print("  ________  \n"
                      "  |       |  \n"
                      "  |       |  \n"
                      "  |       |  \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n"
                      "__|__        \n")

            elif count == 3:
                print()
                print("wrong input, You are hanged!")
                print("  ________  \n"
                      "  |       |  \n"
                      "  |       |  \n"
                      "  |       |  \n"
                      "  |       O  \n"
                      "  |      /|\ \n"
                      "  |      / \ \n"
                      "  |          \n"
                      "__|__        \n")

        if word == "*" * length:
            print("Congrats, you have guessed it successfully")

        elif count != limit:
            hangman(count, display, word)
    else:
        print()
        print("Attention:\nYou are not allowed to guess two letter at the same time")
        print()
        hangman(count, display, word)


hangman(count, display, word)


# i finally create a hangman, so the things i will do now is to improve it. my favorite part

"""i did some updating inside the game, i hope you enjoy it.
   author: @TommySylver
"""


