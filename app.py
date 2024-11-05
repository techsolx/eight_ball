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

result_num = random.randint(0, 19)


def ask_question():
    question = input("What is your question? ")
    if "?" in question:
        return True
    else:
        print("Please phrase your question in the form of a question - ?")


answer = responses[result_num]
response = ask_question()

if response:
    print(answer)
else:
    ask_question()
