# Queue Management System (QueueEase)

## Project Overview
QueueEase is a Python-based desktop queue management system designed to manage customer queues in service-oriented environments such as banks, hospitals, and offices. The system replaces manual queue handling with a digital token-based approach to improve efficiency and reduce waiting time.

The application provides separate interfaces for customers and staff, ensuring clear role-based functionality and smooth queue operations.

---

## Objectives
- Reduce customer waiting time
- Improve service efficiency
- Digitize the queue handling process
- Provide a simple and user-friendly graphical interface

---

## User Roles and Features

### Customer
- Register and log in
- Generate a queue token
- View current token status
- See which token is currently being served
- Log out securely

### Staff
- Log in as staff
- View pending tokens
- Call the next token
- Mark tokens as completed
- Reset the queue
- Log out securely

---

## Technologies Used
- Python
- Tkinter (GUI)
- SQLite
- Git & GitHub

---

queue-management-system/
├── main.py
├── auth.py
├── database.py
├── customer.py
├── staff.py
├── token_manager.py
├── README.md
├── .gitignore


---

## Database Handling
- SQLite is used as the database.
- Database tables are created automatically at runtime.
- The database file is not included in the repository to avoid conflicts in a team environment.

---

## How to Run the Project
1. Install Python 3.x
2. Clone the repository:
   git clone https://github.com/prateeksatyal/queue-management-system.git
3. Navigate to the project folder:
   cd queue-management-system
4. Run the application:
   python main.py

---

## Limitations
- Desktop-based application only
- Basic authentication (academic purpose)
- No network-based multi-user support

---

## Future Improvements
- Token priority support
- Better UI design
- Reports and analytics
- Web-based version

---

## Team Roles and Responsibilities

### Team Leader
**Prateek Satyal**
- Overall project coordination and planning
- Designed the system architecture
- Integrated all modules into the main application
- Managed GitHub repository and version control
- Reviewed and finalized project documentation

---

### Team Members

**Aryanshah Thakuri**
- Developed user authentication module (`auth.py`)
- Implemented login and registration functionality
- Assisted in input validation and error handling
- Contributed to documentation improvements

**Ritesh Chand**
- Designed and implemented database layer (`database.py`)
- Created database schema and table creation logic
- Managed SQLite integration and data handling
- Assisted in debugging database-related issues

**Rajip**
- Developed queue and token management logic (`token_manager.py`)
- Implemented token generation, serving, and completion logic
- Assisted in staff-side functionality (`staff.py`)
- Helped with UI testing and validation

---

### Collaborative Work
- All team members participated in testing and debugging
- Documentation and UI improvements were done collaboratively
- GitHub was used for team collaboration and version control

---

## Academic Note
This project is developed for educational purposes as part of a software design coursework. Security features are simplified for learning purposes.

---

## Conclusion
QueueEase demonstrates the application of software engineering principles, GUI development, database integration, and team-based version control practices.
   

