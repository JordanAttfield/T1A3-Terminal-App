from quiz import Question
import random

def welcome():
    print("\nWelcome to Blind Date with a Book!\n")
    print("Please begin by completing our quiz to determine your reading preferences. Alternatively you can select a book yourself.")
    print("1. Take Quiz")
    print("2. I'd like to choose a book myself")
    print("3. Quit")
    option = input("Please select your option (1, 2 or 3): ")
    return option

book_questions = [
    "What kind of movie is your favourite?\n(a)  Romance - The Notebook is a favourite!\n(b) I honestly couldn't pick - I love a broad range of everything!\n(c) Suspenseful movies with creepy twists\n\n",
    "What's your ideal setting?\n(a) Somewhere warm and cozy where I can curl up with a book\n(b) Somewhere that's just asking to be explored!\n(c) Somewhere creepy and secluded\n\n",
    "Who would you like to have dinner with?\n(a) Augustus Waters\n(b) Hermione Granger\n(c) Sherlock Holmes\n\n"
]

questions = [
    Question(book_questions[0]),
    Question(book_questions[1]),
    Question(book_questions[2])
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == "a":
            score += 1
        elif answer == "b":
            score += 2
        elif answer == "c":
            score += 3
    return score


def genre_selection(score):
    if score <= 4:
        print("Looks like you're in the mood for an Historical Fiction book!\n Please see your book selection below:")
    elif (score >= 5) and (score <= 7):
        print("Looks like you're in the mood for an Historical Fiction book!\n Please see your book selection below:")
    elif (score >= 8) and (score <= 9):
        print("Looks like you're in the mood for an Historical Fiction book!\n Please see your book selection below:")


user_choice = ""

while user_choice != 3:
    user_choice = welcome()

    if user_choice == "1":
        run_quiz(questions)
    elif user_choice == "2":
        pass
    elif user_choice == "3":
        break