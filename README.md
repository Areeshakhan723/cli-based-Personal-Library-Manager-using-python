# cli-based-Personal-Library-Manager-using-python

A simple command-line application to manage a personal library of books. This tool allows users to manage their book collection by adding, removing, and searching for books. Each book is stored as a dictionary with details like title, author, publication year, genre, and read status. The program includes a menu system, basic statistics, and optional file handling for saving and loading the library.

---

## Features

- **Add Books:** Add a new book to the library by providing details such as title, author, publication year, genre, and read status.
- **Remove Books:** Delete a book from the library by specifying its title.
- **Search Books:** Search for books by title or author.
- **Update Books:** Modify the details of an existing book.
- **View All Books:** Display a list of all books in the library with their details.
- **Reading Progress:** View basic statistics about your reading progress, such as the total number of books and the percentage of books you've read.
- **File Handling:** Save and load the library to/from a JSON file for persistent storage.

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

