import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""
    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []  # List to store books
        self.storage_file = "book_data.json" # File to save book data
        self.read_file()  # Load existing books from the file


    def read_file(self):
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file: 
                self.book_list = json.load(file)  # Load books from the file
        except (FileNotFoundError, json.JSONDecodeError): 
            self.book_list = [] # If file doesn't exist or is invalid, start fresh


    def save_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4) # Save books to the file



    def create_new_file(self):
        """Add a new book to the collection by gathering information from the user."""
        # Get book details from the user
        book_title = input("Enter book name: ")
        book_author = input("Enter the author of book:")
        publication_year = input("Enter the publication year:")
        book_genre = input("Enter the genre:")
        is_book_read = (input("Have you read this book? (yes/no): ").strip().lower() == "yes")
    
        # Create a dictionary for the new book
        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book) # Add the new book to the list
        self.save_file()  # Save the updated list to the file
        print("Book added successfully!\n")


    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove:")

         # Search for the book by title and remove it
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_file()  # Save the updated list to the file
                print("Book delete successfully!")
                return        
        print("Book not found\n") # If book is not found

    
    def show_all_books(self):
        """Display all books in the collection with their details."""
        if not self.book_list:
            print("Your collection is empty.\n")
            return
        
         # Print details of each book
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(f'{index}: {book["title"]} by {book["author"]} ({book['year']}) - {book['genre']} - {reading_status}')
        print()


    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by \n1. Book title  \n2. Author\nEnter your choice: ")
        search_text = input("Enter search tearm: ").lower()

        # Find books matching the search term
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]


        if found_books:
            print("Maching books")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f'{index}: {book["title"]} by {book["author"]} ({book['year']}) - {book['genre']} - {reading_status}')
        else:
            print("No matching books found.\n")

               
    def update_books(self):
        """Modify the details of an existing book in the collection."""
        book_title = input("Enter the title of the book you want to edit: ")

         # Search for the book by title
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")

                # Update book details if new input is provided
                book["title"] = input(f"New title ({book['title']}): ") or book['title']
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"
                )
                 # Save the updated list to the file
                self.save_file()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")  


    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        total_books = len(self.book_list)  # Total number of books
        completed_books = sum(1 for book in self.book_list if book["read"]) # Number of read books
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0  # Calculate progress
        )
         
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")


    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7)")

            # Handle user choice
            if user_choice == "1":
                self.create_new_file()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_books()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_file()  # Save data before exiting
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")



if __name__ == "__main__":
    book_manager = BookCollection()  # Create an instance of BookCollection
    book_manager.start_application() # Start the application