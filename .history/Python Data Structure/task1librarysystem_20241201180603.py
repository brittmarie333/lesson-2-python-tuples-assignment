#You are maintaining a library system where each book is stored as a tuple within a list.
#Your task is to update this system by adding new books and ensuring no duplicates.
#Existing Library Data:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.
def add_book(book_title, book_author):
    new_book = (book_title, book_author)


    
 if new_book in library:
        print(f"The book '{book_title}' by {book_author} already exists in the library.")
    else:
        library.append(new_book)
        print(f"'{book_title}' by {book_author} has been added to the library.")