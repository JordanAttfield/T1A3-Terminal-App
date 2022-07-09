def welcome():
    print("\nWelcome to Book Box!\n")
    print("Please Login or Register")
    print("1. Login")
    print("2. Register")
    print("3. Quit")
    option = input("Please select your option (1, 2 or 3): ")
    return option


def book_selection():
    print("Please select which genre books you'd like to receive in your next Book Box!")


book_catalogue = {
    "Popular Fiction": ["The Seven Husbands of Evelyn Hugo by Taylor Jenkins Reid", "Anxious People by Fredrik Backman", "The Four Winds by Kristin Hannah", "Where The Crawdads Sing by Delia Owens"]
    "Thriller": ["The Lies I Tell by Julie Clark", "Things We Do In The Dark by Jennifer Hillier", "The House Across The Lake by Riley Sager", "The Family Upstairs by Lisa Jewell"]
    "Romance": ["People We Meet on Vacation by Emily Henry", "The Unhoneymooners by Christina Lauren", "Every Summer After by Carley Fortune", "One Italian Summer by Rebecca Serle"]
    "Fantasy": ["This Time Tomorrow by Emma Straub", "The Cruel Prince by Holly Black", "Circe by Madeline Miller", "House of Sky and Breath by Sarah J Maas"] 
}

names = []
usernames = []
passwords = []

def register():
    names.append(input("Please enter your name: "))
    usernames.append(input("Please choose a username: "))
    passwords.append(input("Please choose a password: "))


def login():
    username = input("Please enter your username: ")
    password = input("Please enter your Password: ")
    if username in usernames and password in passwords:
        print("welcome")
    else:
        print("incorrect!")

user_choice = ""

while user_choice != 3:
    user_choice = welcome()
    if user_choice == "1":
        register()
    elif user_choice == "2":
        login()
    elif user_choice == "3":
        break