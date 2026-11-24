# club-attendance-gui-app-project - Demi, Fatima, Kiana, Delilah - CCT211 Project 2

# Club Meets 
The university club attendance manager application, Club Meets, allows club executives to track attendance for events and meetings in one place – a more efficient alternative to paper or multi-sheet Excel files. Club Meets allows executives to create events, record attendance, and review participation, while members can view upcoming events and RSVP. A successful version of Club Meets will provide a functional, user-friendly application that simplifies university club management. Executives should be able to efficiently manage members, create events, record attendance, and monitor participation. Members should be able to view upcoming events, RSVP, and track their personal attendance. The application should have a clear and consistent interface, reliable data storage, and accurate attendance calculations. We aim to create a well-organized, maintainable code with appropriate error handling and automated tests to ensure the application functions reliably.

# Contribution
Demi: Login page, Executive events management page
Kiana: Members events page
Fatima: Roster page
Delilah: Personal attendance page (members)

# Tech Stack 
We used Python and Tkinter to build this application. The data will persist in an SQLite database with Python’s sqlite3 module. The code will be organized into separate classes: model classes (Member, Event, etc.), one window class per page, and a database manager for all queries. To more efficiently test our code logic, we will separate the logic code from the GUI code, using pytest for the database and attendance logic. We will ensure to include PEP8 checked with flake8, docstrings, a GitHub README, and commits to our shared repository. 
