from questions import Question
import random
from seed import book_catalogue
from os import system
from addons import Addons
from functools import reduce

# Welcome message and menu options
def welcome():
    print("\nWelcome to Blind Date with a Book!\n")
    print(
        "Please begin by completing our quiz to determine your reading preferences. Alternatively you can select a book yourself.")
    print("1. Take Quiz")
    print("2. I'd like to choose a book myself")
    print("3. Extra goodies to go with your new books")
    print("4. View Cart")
    print("5. Quit")
    option = input("Please select your option (1 - 5): ")
    return option

# Questions for quiz 
book_questions = [
    "What kind of movie is your favourite?\n(a)  Romance - The Notebook is a favourite!\n(b) I honestly couldn't pick - I love a broad range of everything!\n(c) Suspenseful movies with creepy twists\n\n",
    "What's your ideal setting?\n(a) Somewhere warm and cozy where I can curl up with a book\n(b) Somewhere that's just asking to be explored!\n(c) Somewhere creepy and secluded\n\n",
    "Who would you like to have dinner with?\n(a) Augustus Waters\n(b) Hermione Granger\n(c) Sherlock Holmes\n\n"
]

add_on1 = Addons("Penfolds Shiraz", "Enjoy a glass of red wine while you dive into your book. An initial aroma of warm spice and dark red fruits, pronounced with tastes of mulberry and blackberry supported by subtle oak", 30.0)
add_on2 = Addons("Haighs Chocolates Small Hamper Box", "Indulge in a selection of Haighs most popular chocolates", 15.0)
add_on3 = Addons("Book Lovers Candle", "Enjoy the aromas of dusty tomes and leather bound books while you read", 10)
add_on4 = Addons("Byron Bay Gourmet Drinking Hot Chocolate", "Sip a mug of rich, velvety hot chocolate", 8)

add_on_selection = [add_on1, add_on2, add_on3, add_on4]

# Selects book genre based on quiz results. Prints message and randomly selects book from dictionary. Gives option to checkout.
def popular_fiction():
    print(
        "Looks like you're in the mood for a Popular Fiction book!\n\nPlease see the book we have selected for you below:\n")
    chosen_book = random.choice(book_catalogue["fiction"])
    print(chosen_book)
    checkout(chosen_book, cart, cart_total)
    return chosen_book


def romance():
    print("Looks like you're in the mood for a Romance book!\n\nPlease see the book we have selected for you below:\n")
    chosen_book = random.choice(book_catalogue["romance"])
    print(chosen_book)
    checkout(chosen_book, cart, cart_total)
    return chosen_book


def thriller():
    print("Looks like you're in the mood for a Thriller book!\n\nPlease see the book we have selected for you below:\n")
    chosen_book = random.choice(book_catalogue["thrillers"])
    print(chosen_book)
    checkout(chosen_book, cart, cart_total)
    return chosen_book

# Questions for quiz
questions = [
    Question(book_questions[0]),
    Question(book_questions[1]),
    Question(book_questions[2])
]

# Checkout option once book selections have been generated. Gives option to add to cart.
cart = []
cart_total = 0

def checkout(chosen_book, cart, cart_total):
    checkout_ans = input("\nPlease confirm your purchase by typing 'yes' or 'no'. The price of all our new releases is $18 per book.\n Choose no to redo the quiz.")
    if checkout_ans == "yes":
        cart.append(chosen_book)
        cart_total += 18
        print(f"\nHere is your shopping cart:\n{cart}")
        print(f"Cart Total: ${cart_total}")
    elif checkout_ans == "no":
        print("Let's try the quiz again!\n")
        run_quiz(questions)
    return cart, cart_total
    

# Add ons function to add additional products to cart
def addon_item():
    answer = input("Would you like to add one of our goodies? (Type 'yes' or 'no'")
    if answer == "yes":
        print(add_on1)
        print(add_on2)
        print(add_on3)
        print(add_on4)

# Option from main menu that lists entire book catalogue and gives option to add books to cart
def add_book():
    print("Here is our selection of books: \n")
    flatlist = reduce(lambda a,b:a+b, book_catalogue.values())
    print(flatlist)
    chosen_book = None
    while chosen_book not in flatlist:
        chosen_book = input("\nPlease type the name of the book you'd like to purchase: ")
        print("That book isn't in our selection. Please try again.")
    checkout(chosen_book, cart, cart_total)
    
# Determining quiz score which is used to determine genre preference and book selection
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

def view_cart():
    pass

user_choice = ""

while user_choice != 3:
    system('clear')
    user_choice = welcome()
    if user_choice == "1":
        run_quiz(questions)
    elif user_choice == "2":
        add_book()   
    elif user_choice == "3":
        addon_item()
    elif user_choice == "4":
        view_cart()
    elif user_choice == "5":
        print("See you next time!")
    else:
        print("Invalid option. Please try again.")

    input("\nPress enter to return to the main menu")
    system('clear')


