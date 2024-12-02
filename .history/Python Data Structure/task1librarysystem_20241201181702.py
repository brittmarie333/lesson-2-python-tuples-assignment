#You are maintaining a library system where each book is stored as a tuple within a list.
#Your task is to update this system by  adding new books and ensuring no duplicates.
#Existing Library Data:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

def add_book_to_library(library, new_book):
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{new_book[0]}' by {new_book[1]} added to the library.")
    else:
        print(f"Book '{new_book[0]}' by {new_book[1]} is already in the library.")

def view_library(library):
    print("\nCurrent Library:")
    for book in library:
        print(f"Title: {book[0]}, Author: {book[1]}")

def main():
    while True:
        title = input("Enter book title (or type 'exit' to view current library): ")
        if title.lower() == 'exit':
            view_library(library)
            break
        author = input("Enter book author: ")
        
        new_book = (title, author)
        add_book_to_library(library, new_book)

if __name__ == "__main__":
    main()