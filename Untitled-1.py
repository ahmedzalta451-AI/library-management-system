class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


    def borrow(self):
        if self.available:
            self.available = False
            print(f"\nYou borrowed '{self.title}'")
        else:
            print("\nBook is already borrowed")


    def return_book(self):
        if not self.available:
            self.available = True
            print(f"\nYou returned '{self.title}'")
        else:
            print("\nThis book was not borrowed")


class Library:

    def __init__(self):
        self.books = [
            Book("Clean Code", "Robert C. Martin"),
            Book("Python Crash Course", "Eric Matthes"),
            Book("Automate the Boring Stuff with Python", "Al Sweigart"),
            Book("The Pragmatic Programmer", "Andrew Hunt"),
            Book("Introduction to Algorithms", "Thomas H. Cormen"),
            Book("Design Patterns", "Erich Gamma"),
            Book("Artificial Intelligence: A Modern Approach", "Stuart Russell"),
            Book("Deep Learning", "Ian Goodfellow")
        ]


    def show_books(self):

        print("\n===== Available Books =====")

        for i, book in enumerate(self.books):

            status = "Available" if book.available else "Borrowed"

            print(f"{i+1}. {book.title} - {book.author} ({status})")


    def borrow_book(self):

        self.show_books()

        try:
            num = int(input("\nEnter book number: ")) - 1

            if 0 <= num < len(self.books):
                self.books[num].borrow()
            else:
                print("Invalid number")

        except ValueError:
            print("Please enter a valid number")


    def return_book(self):

        self.show_books()

        try:
            num = int(input("\nEnter book number to return: ")) - 1

            if 0 <= num < len(self.books):
                self.books[num].return_book()
            else:
                print("Invalid number")

        except ValueError:
            print("Please enter a valid number")


    def search_book(self):

        keyword = input("\nEnter book title or author: ").lower()

        found = False

        for book in self.books:

            if keyword in book.title.lower() or keyword in book.author.lower():

                status = "Available" if book.available else "Borrowed"

                print(f"{book.title} - {book.author} ({status})")

                found = True

        if not found:
            print("No matching book found")


def main():

    library = Library()

    while True:

        print("\n===== Library Management System =====")

        print("1. Show Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.show_books()

        elif choice == "2":
            library.borrow_book()

        elif choice == "3":
            library.return_book()

        elif choice == "4":
            library.search_book()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()































































































    