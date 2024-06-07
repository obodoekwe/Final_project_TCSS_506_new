import requests


def query_open_library():
    # Query Open Library API for books on a specific subject
    url = "https://openlibrary.org/search.json?q=subject:book"
    response = requests.get(url)
    data = response.json()

    # Extract book details and create a dictionary
    books = {}
    for doc in data.get("docs", []):
        title = doc.get("title", "")
        authors = doc.get("author_name", [])
        author = ", ".join(authors) if isinstance(authors, list) else authors
        cover_id = doc.get("cover_i")
        image_url = f"http://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else None
        description = doc.get("description", "")
        if title:
            books[title] = {
                'title': title,
                'author': author,
                'image_url': image_url,
                'description': description
            }

    # Sort the dictionary by title names
    sorted_books = dict(sorted(books.items(), key=lambda item: item[0]))
    return sorted_books


def get_book_by_title(title):
    # Retrieve the dictionary of books
    books = query_open_library()
    # Return the book with the given title, or None if not found
    return books.get(title)


if __name__ == "__main__":
    sorted_books_dict = query_open_library()
    print(sorted_books_dict)

