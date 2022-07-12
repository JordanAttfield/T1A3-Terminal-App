from email.charset import add_codec


class Addons:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return self.name, self.description, self.price

add_on1 = Addons("Penfolds Shiraz", "Enjoy a glass of red wine while you dive into your book. An initial aroma of warm spice and dark red fruits, pronounced with tastes of mulberry and blackberry supported by subtle oak", 30.0)
add_on2 = Addons("Haighs Chocolates Small Hamper Box", "Indulge in a selection of Haighs most popular chocolates", 15.0)
add_on3 = Addons("Book Lovers Candle", "Enjoy the aromas of dusty tomes and leather bound books while you read", 10)
add_on4 = Addons("Byron Bay Gourmet Drinking Hot Chocolate", "Sip a mug of rich, velvety hot chocolate", 8)

add_on_selection = [add_on1, add_on2, add_on3, add_on4]