#This is a hash bang #!
#!/usr/bin/env python3

import random

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

len_responses = len(responses)
# Ways to get a random number from zero the the length of the responses list
# rand_response = random.randint(0, len_responses - 1)
rand_response = random.randrange(0, len_responses)


def ask_question():
    question = input("What is your question? ")
    if "?" in question:
        return True
    else:
        print("Please phrase your question in the form of a question - ?")


answer = responses[rand_response]
# Another way to get a random.choice from a list
#answer = random.choice(responses)
response = ask_question()

if response:
    print(answer)
else:
    ask_question()
