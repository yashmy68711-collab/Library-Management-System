class Library:
    def __init__(self):
        self.books = ["Python", "AI Basics", "Robotics", "Math"]

    def view_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You borrowed '{book_name}'")
        else:
            print("Book not available")

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