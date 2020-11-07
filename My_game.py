class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Questions():
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


prompts = ["What is the color of the sky.\na)yellow \nb)gray \nc) blue\n--> ",
           "\nWhat is something that each person have personally\n--> ",
           "\nthis is an expression, fill out the blank:\nWhen pigs ___\n--> ",
           "\ncan you give a song's title where there is this word\na) slide\n--> ",
           "\nb) man\n--> ",
           "\nc) life\n--> "
           ]

questions = [Questions(prompts[0], "c"),
             Questions(prompts[1], "name"),
             Questions(prompts[2], "fly"),
             Questions(prompts[3], "toosie slide"),
             Questions(prompts[4], "when i was your man"),
             Questions(prompts[5], "this is your life")]


names = input("What's your name?\n--> ")
ages = input("How old are you?\n--> ")

the_student = Student(names, ages)

count = 0
for question in questions:

    answer = input(question.prompt)
    if answer == question.answer:
        count += 1
        print("--> Good Job")
    else:
        print("--> You are such a bengy")

print(count)

if count >= len(questions)/2:
    print("Pretty good " + the_student.name)
else:
    print("try again")
    print("Grow up a little bit.")





