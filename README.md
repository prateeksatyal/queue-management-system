# Queue Management System (QueueEase)

## Project Overview
QueueEase is a Python-based desktop queue management system developed as part of the **ST4008CEM – Computing Activity Led Learning (Project 1)** module. The system is designed to manage customer queues in service-oriented environments such as banks, hospitals, and offices.

The application replaces manual queue handling with a digital token-based approach to improve efficiency, reduce waiting time, and enhance the overall service experience. Separate interfaces are provided for customers and staff to ensure clear role-based functionality.

---

## Objectives
- Reduce customer waiting time
- Improve service efficiency
- Digitize the queue handling process
- Provide a simple and user-friendly graphical interface
- Apply practical programming and team collaboration skills

---

## User Roles and Features

### Customer
- Register and log in to the system
- Generate a queue token
- View current token status
- See which token is currently being served
- Log out securely

### Staff
- Log in as staff
- View all pending tokens
- Call the next token in the queue
- Mark tokens as completed
- Reset the queue when required
- Log out securely

---

## Technologies Used
- **Programming Language:** Python
- **GUI Framework:** Tkinter
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## Project Structure
queue-management-system/
├── main.py # Application entry point and UI routing
├── auth.py # User authentication (login & registration)
├── database.py # Database connection and table creation
├── customer.py # Customer dashboard and token actions
├── staff.py # Staff dashboard and queue control
├── token_manager.py # Core queue and token management logic
├── README.md # Project documentation
├── .gitignore # Files excluded from version control



This structure improves readability, maintainability, and supports team-based development.

---

## Database Handling
- SQLite is used as the database.
- Database tables are created automatically at runtime.
- The database file is not included in the repository to avoid conflicts in a team environment.

This approach follows good practices for collaborative development.

---

## How to Run the Project
1. Ensure Python 3.x is installed on your system.
2. Clone the repository:
   git clone https://github.com/prateeksatyal/queue-management-system.git

3. Navigate to the project directory:
   cd queue-management-system

4. Run the application:
   python main.py


The database will be created automatically on first execution.

---

## Limitations
- Desktop-based application only
- Basic authentication for academic purposes
- No network-based multi-user support

---

## Future Improvements
- Token priority support
- Improved user interface design
- Reports and analytics dashboard
- Web-based version of the system
- Enhanced security features

---

## Team Roles and Responsibilities

### Team Leader
**Prateek Satyal**
- Overall project coordination and planning
- Designed the system architecture
- Integrated all modules into the main application
- Managed GitHub repository and version control
- Reviewed and finalized project documentation

### Team Members

**Aryanshah Thakuri**
- Developed the user authentication module (`auth.py`)
- Implemented login and registration functionality
- Assisted in input validation and error handling
- Contributed to documentation improvements

**Ritesh Chand**
- Designed and implemented the database layer (`database.py`)
- Created database schema and table creation logic
- Managed SQLite integration and data handling
- Assisted in debugging database-related issues

**Rajip**
- Developed queue and token management logic (`token_manager.py`)
- Implemented token generation, serving, and completion logic
- Assisted in staff-side functionality (`staff.py`)
- Helped with UI testing and validation

### Collaborative Work
- All team members participated in testing and debugging
- Documentation and UI improvements were done collaboratively
- GitHub was used for team collaboration and version control

---

## Academic Note
This project is developed for **ST4008CEM – Computing Activity Led Learning (Project 1)**.  
The focus of the project is on practical implementation, teamwork, and applying programming concepts learned during the module.

---

## Conclusion
QueueEase demonstrates the practical application of Python programming, GUI development, database integration, and collaborative version control. The project fulfills the objectives of the **Computing Activity Led Learning** module by emphasizing hands-on development and team-based problem solving.

The project follows a modular structure where each file handles a specific responsibility.

