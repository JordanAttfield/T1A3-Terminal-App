from questions import Question
import random
from seed import book_catalogue
from os import system


def welcome():
    print("\nWelcome to Blind Date with a Book!\n")
    print(
        "Please begin by completing our quiz to determine your reading preferences. Alternatively you can select a book yourself.")
    print("1. Take Quiz")
    print("2. I'd like to choose a book myself")
    print("3. Quit")
    option = input("Please select your option (1, 2 or 3): ")
    return option

def popular_fiction():
    print(
        "Looks like you're in the mood for a Popular Fiction book!\n\nPlease see the book we have selected for you below:\n")
    print(random.choice(book_catalogue["fiction"]))


def romance():
    print("Looks like you're in the mood for a Romance book!\n\nPlease see the book we have selected for you below:\n")
    print(random.choice(book_catalogue["romance"]))


def thriller():
    print("Looks like you're in the mood for a Thriller book!\n\nPlease see the book we have selected for you below:\n")
    print(random.choice(book_catalogue["thrillers"]))


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


def add_book():
    print("Here is our selection of books: \n")
    for key, value in book_catalogue.items():
        print(key, *value, sep='\n')


def add_on_items():
    answer = input("Would you like to add on any goodies to your book purchase?\nPrint 'Yes' or 'No'")
    if answer == "yes":
           
        


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
    determine_genre(score)
    return score


def determine_genre(score):
    if score <= 4:
        romance()
    elif (score >= 5) and (score <= 7):
        popular_fiction()
    elif (score >= 8) and (score <= 9):
        thriller()


user_choice = ""

while user_choice != 3:
    system('clear')
    user_choice = welcome()
    system('clear')
    if user_choice == "1":
        run_quiz(questions)
    elif user_choice == "2":
        add_book()
    elif user_choice == "3":
        continue
    else:
        print("Invalid option. Please try again.")

    input("\nPress enter to return to the main menu")
    system('clear')

print("See you next time!")
