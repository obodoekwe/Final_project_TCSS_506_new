Final_project_TCSS_506 repository is created for group capstone project(Book wishlist web app) by Team 4. This text file
below provides brief discription on the structure of the project.

# html files

base.html: The template features a navigational bar that adapts based on user session state, displaying relevant
options such as logout for authenticated users. It also establishes a visual theme with a custom-styled background
and a centralized content area where specific page content is dynamically injected, ensuring a uniform look while
allowing flexibility for page-specific designs.

home.html: It extends the foundational base.html to maintain a consistent layout and style, featuring a welcoming
header that reaffirms the application's purpose and user-oriented navigation. This page is designed to be the hub
of user activity, allowing users to manage their book wishlist efficiently.

landing.html: Extending base.html, the design utilizes a clean, centered layout that presents two large buttons—each
leading to either the login or registration page—facilitated by intuitive navigation aided by Bootstrap's responsive
design elements.

login.html & register.html: Provide user-friendly interfaces for authentication processes. Both templates extend
the common layout defined in base.html, ensuring consistency in appearance and navigation across the site.

book_details.html: Extending base.html, it shows detailed attributes of a book such as title, author, description,
and an image.

wishlist.html: Extending from the base.html for consistent layout and design, this template specifically focuses
on providing a personalized experience by listing all the books a user has added to their wishlist

# Python files

app.py: The Flask file serves as the core server-side script for your Book Wishlist application, orchestrating
web requests, user session management, and interactions with the database.

book.py: The book.py file is a critical component of the Book Wishlist application, functioning as a bridge
between the Open Library API and the Flask web app. It facilitates the retrieval and organization of book data,
which is crucial for populating the application with dynamic content.

forms.py: Utilizes Flask-WTF to create forms for login and registration, ensuring validation and secure data
handling.

models.py: Contains SQLAlchemy models for User and Book, as well as methods for setting and checking passwords
using password hashing, detailing how these entities are stored in the database, including relationships such
as users having a list of books.

# Docker deployment

To deploy with docker, use:
docker-compose --profile test up -d
