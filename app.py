from ast import Continue
from questions import Question
import random
from seed import book_catalogue
import os
from addons import Addons
from functools import reduce
from colorama import Fore

# Welcome message and menu options
def welcome():
    print(Fore.MAGENTA + "\nWelcome to Blind Date with a Book!\n")
    print(
        "Please begin by completing our quiz to determine your reading preferences.\nAlternatively you can select a book yourself.\n")
    print("1. Take Quiz")
    print("2. I'd like to choose a book myself")
    print("3. Extra goodies to go with your new books")
    print("4. View Cart")
    print("5. Quit")
    option = input("Please select your option (1 - 5): ")
    os.system('clear')
    return option
     

# Questions for quiz 
book_questions = [Fore.LIGHTBLUE_EX +
    "What kind of movie is your favourite?\n(a)  Romance - The Notebook is a favourite!\n(b) I honestly couldn't pick - I love a broad range of everything!\n(c) Suspenseful movies with creepy twists\n\n",
    "What's your ideal setting?\n(a) Somewhere warm and cozy where I can curl up with a book\n(b) Somewhere that's just asking to be explored!\n(c) Somewhere creepy and secluded\n\n",
    "Who would you like to have dinner with?\n(a) Augustus Waters\n(b) Hermione Granger\n(c) Sherlock Holmes\n\n"
]

add_on1 = Addons("Red Wine","\nEnjoy a glass of red wine while you dive into your book", 30.0)
add_on2 = Addons("Box of Chocolates", "\nIndulge in a selection of Haighs most popular chocolates", 15.0)
add_on3 = Addons("Book Lovers Candle", "\nEnjoy the aromas of dusty tomes and leather bound books while you read", 10)
add_on4 = Addons("Hot Chocolate Mix", "\nSip a mug of rich, velvety hot chocolate", 8)

add_on_selection = [add_on1, add_on2, add_on3, add_on4]

# Selects book genre based on quiz results. Prints message and randomly selects book from dictionary. Gives option to checkout.
def popular_fiction():
    os.system('clear')
    print(
        "Looks like you're in the mood for a Popular Fiction book!\nPlease see the book we have selected for you below:\n")
    chosen_book = random.choice(book_catalogue["fiction"]) 
    print(chosen_book)
    print("\nWould you like to purchase? All new releases are $18")
    checkout(chosen_book, cart)
    return chosen_book


def romance():
    os.system('clear')
    print("Looks like you're in the mood for a Romance book!\nPlease see the book we have selected for you below:\n")
    chosen_book = random.choice(book_catalogue["romance"])
    print(chosen_book)
    print("\nWould you like to purchase? All new releases are $18")
    checkout(chosen_book, cart)
    return chosen_book


def thriller():
    os.system('clear')
    print("Looks like you're in the mood for a Thriller book!\nPlease see the book we have selected for you below:\n")
    chosen_book = random.choice(book_catalogue["thrillers"])
    print(chosen_book)
    print("\nWould you like to purchase? All new releases are $18")
    checkout(chosen_book, cart)
    return chosen_book

# Questions for quiz
questions = [
    Question(book_questions[0]),
    Question(book_questions[1]),
    Question(book_questions[2])
]

# Checkout option once book selections have been generated. Gives option to add to cart. Error checks to ensure input == 'yes' or 'no'
cart = []
chosen_book = []

def checkout(chosen_book, cart):
    while True:
        checkout_ans = input("\nPlease confirm your purchase by typing 'yes' or 'no'\n")
        if checkout_ans == "yes":
            cart.append(chosen_book)
            print(f"\nHere is your shopping cart:\n{cart}")
            return cart, chosen_book
        elif checkout_ans == "no":
            print("\nYour selected book was not added.\nKeep looking for something else you might like from our selection!\n")
            break
        else: 
            print("Input not recognised")
        


# Add ons function to add additional products to cart 
def addon_item(cart):
    print("Here's a selection of some of our goodies you can purchase:\n")
    for item in add_on_selection:
        print(item)
    while True:
        product = input("\nPlease enter the name of the product you'd like to purchase: ")
        if any(item.name == product for item in add_on_selection):
            cart.append(product)
            print("\nAdded to cart!")
            break
        else:
            print("Sorry that item isn't in our selection. Please try again.")
   

# Option from main menu that lists entire book catalogue and gives option to add books to cart - includes error testing to check chosen book input is in list. 
def add_book():
    print("Here is our selection of books: \n")
    flatlist = reduce(lambda a,b:a+b, book_catalogue.values())
    print(*flatlist, sep="\n")
    while True:
        chosen_book = input("\nPlease type the name of the book you'd like to purchase: ")
        book_choice = False
        for i in flatlist:
            if chosen_book == i:
                book_choice = True
        if book_choice == True:
            checkout(chosen_book, cart)
            break
        else:
            print("We don't have that book in our selection. Please try again.")
            continue
    return chosen_book
       
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
    

def view_cart(cart):
    print("Here is your shopping cart:\n")
    print(*cart, sep="\n")

user_choice = ""

while user_choice != 3:
    os.system('clear')
    user_choice = welcome()
    if user_choice == "1":
        run_quiz(questions)
    elif user_choice == "2":
        add_book()   
    elif user_choice == "3":
        addon_item(cart) 
    elif user_choice == "4":
        view_cart(cart)
    elif user_choice == "5":
        print("See you next time!")
    else:
        print("Invalid option. Please try again.")
        
    input("\nPress enter to return to the main menu")
    


