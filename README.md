# Rally Driver Stats Application

This is a Python-based application for managing rally driver statistics using a graphical user interface (GUI) built with Tkinter. The app allows users to manage data related to **drivers**, **tracks**, **venues**, and **cars** by performing operations such as adding and deleting records. 

## Features

- **Login System**: Users must authenticate using a username and password to access the application.
- **Driver Management**: Add and delete driver records, including name, date of birth, phone number, and driver ID.
- **Track Management**: Add and delete track details like track number and lap number.
- **Venue Management**: Add and delete venue information, including venue ID, name, ticket price, and venue count.
- **Car Management**: Add and delete car data such as car company, name, number, top speed, and car size.
  
## Technologies Used

- **Python**: The application logic is written in Python.
- **Tkinter**: Used to create the graphical user interface (GUI).
- **PyMySQL**: For interacting with a MySQL database to store and manage application data.

## Getting Started

### Prerequisites

1. **Python 3.x** installed on your machine.
2. **MySQL** database running locally or remotely.
3. **PyMySQL** library for connecting the Python application to the MySQL database.

You can install `PyMySQL` via pip:

```bash
pip install pymysql
```

### MySQL Setup

1. Create a MySQL database named `cars2`.
2. Define the required tables for storing data:

```sql
CREATE TABLE Driver (
  Name VARCHAR(255),
  Dob DATE,
  DrivNum VARCHAR(255),
  DrivId INT
);

CREATE TABLE Track (
  TrackNum INT,
  LapNum INT
);

CREATE TABLE Venue (
  VenueId INT,
  VenueName VARCHAR(255),
  VenueTicket INT,
  NumVenue INT
);

CREATE TABLE Car (
  Company VARCHAR(255),
  Name VARCHAR(255),
  CarNum INT,
  SpeedNum INT,
  CarSize VARCHAR(50)
);
```

### Running the Application

1. Clone the repository and navigate to the project directory.
2. Ensure that your MySQL server is running and the required tables are created.
3. Run the `main.py` file using Python:

```bash
python main.py
```

4. The login screen will appear. Use the following default credentials to log in:

    - **Username**: `maaz12`
    - **Password**: `ahmed12`

5. After logging in, you can perform various actions such as managing drivers, tracks, venues, and cars.

## File Structure

```plaintext
.
├── main.py           # Main script with Tkinter GUI and MySQL interaction
├── README.md         # This README file
└── requirements.txt  # List of required Python packages
```

## Screenshots

### Login Screen
![rally driver 1](https://github.com/user-attachments/assets/62cfa27d-8165-402d-bdf0-bcac0c2f8299)

### Main Menu
![Rally driver2](https://github.com/user-attachments/assets/6df8d241-2287-4699-a86a-428e1741264d)

## Future Improvements

- Add an option to update existing records.
- Implement encryption for passwords in the login system.
- Add additional error handling for database connections.

