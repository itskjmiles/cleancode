class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock} copies available")

    def check_availability(self):
        return self.stock > 0

    def sell_copy(self):
        if self.stock > 0:
            self.stock -= 1
            print("Book sold successfully!")
        else:
            print("Sorry, the book is out of stock.")
