import sqlite3

#the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

#existing books are removed
cursor.execute("DROP TABLE IF EXISTS books")

#the books table
cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        genre TEXT,
        copies INTEGER,
        rating INTEGER
    )
""")

# Add one book with a single INSERT statement
cursor.execute(
    "INSERT INTO books (title, author, year, genre, copies, rating) VALUES (?, ?, ?, ?, ?, ?)",
    ("Pride and Prejudice", "Jane Austen", 1813, "Fiction", 4, 5),
)

# Add the rest with a list of tuples and executemany
more_books = [
    ("The Martian", "Andy Weir", 2011, "Fiction", 3, 5),
    ("The Hound of the Baskervilles", "Arthur Conan Doyle", 1902, "Mystery", 2, 4),
    ("Gone Girl", "Gillian Flynn", 2012, "Mystery", 1, None),
    ("A Brief History of Time", "Stephen Hawking", 1988, "Science", 3, 4),
    ("Cosmos", "Carl Sagan", 1980, "Science", 2, None),
    ("Sapiens", "Yuval Noah Harari", 2011, "History", 5, 4),
    ("The Guns of August", "Barbara Tuchman", 1962, "History", 1, 3),
    ("Moby-Dick", "Herman Melville", 1851, "Fiction", 2, 3),
    ("The Silent Patient", "Alex Michaelides", 2019, "Mystery", 3, 4),
]
cursor.executemany(
    "INSERT INTO books (title, author, year, genre, copies, rating) VALUES (?, ?, ?, ?, ?, ?)",
    more_books,
)
conn.commit()

# books published after 1990
print("Title and author of books published after 1990:")
cursor.execute("SELECT title, author FROM books WHERE year > 1990")
for title, author in cursor.fetchall():
    print(f"  {title} by {author}")

# fiction books with more than 2 copies
print("\nFiction books with more than 2 copies:")
cursor.execute("SELECT title FROM books WHERE genre = 'Fiction' AND copies > 2")
for (title,) in cursor.fetchall():
    print(f"  {title}")

# published before 1900 or rated 5 
print("\nBooks published before 1900 or rated 5:")
cursor.execute("SELECT title FROM books WHERE year < 1900 OR rating = 5")
for (title,) in cursor.fetchall():
    print(f"  {title}")

# not in the mystery genre
print("\nBooks that are not in the Mystery genre:")
cursor.execute("SELECT title FROM books WHERE NOT genre = 'Mystery'")
for (title,) in cursor.fetchall():
    print(f"  {title}")

# science or History genre
print("\nBooks in the Science or History genre:")
cursor.execute("SELECT title FROM books WHERE genre IN ('Science', 'History')")
for (title,) in cursor.fetchall():
    print(f"  {title}")

# authors whose names start with a letter the user enters
letter = input("\nEnter a letter: ").strip()
print(f"Authors whose names start with '{letter}':")
cursor.execute("SELECT DISTINCT author FROM books WHERE author LIKE ?", (letter + "%",))
for (author,) in cursor.fetchall():
    print(f"  {author}")

# books with no rating
print("\nBooks that have no rating:")
cursor.execute("SELECT title FROM books WHERE rating IS NULL")
for (title,) in cursor.fetchall():
    print(f"  {title}")

# close the connection
conn.close()
