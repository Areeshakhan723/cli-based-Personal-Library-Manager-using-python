# cli-based-Personal-Library-Manager-using-python
# Personal Library Manager

A simple command-line application to manage a personal library of books. This tool allows you to store, organize, and track your reading progress effortlessly.

---

## Features

The application supports the following features:

- **Add New Books to the Library:**  
  Add a new book by providing details such as title, author, publication year, genre, and reading status.

- **Delete Books from the Library:**  
  Remove a book from your collection by specifying its title.

- **Search for Books in the Library:**  
  Search for books by title or author name.

- **Update Book Information:**  
  Modify the details of an existing book (e.g., title, author, year, genre, or reading status).

- **Show All Books in the Library:**  
  Display a list of all books in your collection, including their details and reading status.

- **Show Reading Progress:**  
  View statistics about your reading progress, including the total number of books and the percentage of books you've completed.

---

## Technologies Used

- **Python**: The core programming language used to build the application.
- **JSON File for Data Storage**: Books are stored in a `book_data.json` file, ensuring data persistence between sessions.

---

## Usage

1. **Run the Application:**  
   Execute the `main.py` file to start the application:
   ```bash
   python main.py


2. **Follow the Instructions:**
Use the menu-driven interface in the terminal to manage your library. The options include:

Adding a new book

Deleting a book

Searching for books

Updating book details

Viewing all books

Checking reading progress

Exiting the application

3  **Example Workflow:**
When you run the application, you'll see a menu like this:

📚 Welcome to Your Book Collection Manager! 📚
1. Add a new book
2. Remove a book
3. Search for books
4. Update book details
5. View all books
6. View reading progress
7. Exit

Enter the number corresponding to the action you want to perform and follow the prompts.

**Example Commands**
**Add a New Book**

Enter book name: 1984
Enter the author of book: George Orwell
Enter the publication year: 1949
Enter the genre: Dystopian
Have you read this book? (yes/no): yes

**Delete a Book**

Enter the title of the book to remove: 1984

**Search for Books**

Search by 
1. Book title  
2. Author
Enter your choice: 1
Enter search term: 1984

**Update Book Information**

Enter the title of the book you want to edit: 1984
Leave blank to keep existing value.
New title (1984): 
New author (George Orwell): 
New year (1949): 
New genre (Dystopian): 
Have you read this book? (yes/no): no

**View Reading Progress**

Total books in collection: 10
Reading progress: 60.00%
Data Storage
The application stores all book data in a JSON file (book_data.json).

This file is automatically created and updated as you add, delete, or modify books.

**Requirements**
Python 3.x

No additional libraries are required.

That's it! You can now manage your library using this simple and intuitive command-line interface. Happy reading! 📚
