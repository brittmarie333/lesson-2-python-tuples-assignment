#You are maintaining a library system where each book is stored as a tuple within a list.
#Your task is to update this system by creating a function adding new books and ensuring no duplicates.
#Existing Library Data:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.


def add_book_to_library(library, new_book):
    # Check if the new book already exists in the library
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{new_book[0]}' by {new_book[1]} added to the library.")
    else:
        print(f"Book '{new_book[0]}' by {new_book[1]} is already in the library.")

def add_books_interactively():
    while True:
        # Ask for the book title and author
        title = input("Enter book title (or type 'exit' to stop): ")
        if title.lower() == 'exit':
            break
        author = input("Enter book author: ")
        
        # Add the new book to the library
        new_book = (title, author)
        add_book_to_library(library, new_book)

# Example: Adding a book interactively
add_books_interactively()

# Display the updated library
print("\nUpdated Library:")
for book in library:
    print(f"Title: {book[0]}, Author: {book[1]}")
