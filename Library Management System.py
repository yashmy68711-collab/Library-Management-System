class Library:
    def __init__(self):
        self.books = ["Python", "AI Basics", "Robotics", "Math"]
        self.history = []

    def view_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
          print("\nAvailable Books:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")
            print("Total Books:", len(self.books))

    def borrow_book(self, book_name):
        found = False

        for book in self.books:
            if book.lower() == book_name.lower():
                self.books.remove(book)
                self.history.append(f"Borrowed: {book}")
                print(f"You borrowed '{book}'")
                found = True
                break

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"You returned '{book_name}'")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' added to library")


library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Add Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.view_books()

    elif choice == "2":
        book = input("Enter book name: ")
        library.borrow_book(book)

    elif choice == "3":
        book = input("Enter book name: ")
        library.return_book(book)

    elif choice == "4":
        book = input("Enter new book name: ")
        library.add_book(book)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
