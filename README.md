# Twende Cab Management System CLI App

## Overview

The **Twende Cab Management System** is a command-line interface (CLI) app built using Python and SQLAlchemy. It allows the user to interact with a cab management system, managing passengers, drivers, cabs, and ride requests. The app supports various operations like registering drivers, assigning cabs, handling ride requests, and more.

### Key Components

- **SQLAlchemy ORM**: Used for mapping Python classes to database tables and performing CRUD operations.
- **alembic**: used for tables migartions.
- **Click**: A package to create command-line interfaces.
- **Database Seeding**: Populating the database with initial data.
- **Commands**: Registering cabs and drivers, viewing records, and deleting entities.

---

## Prerequisites

Before running the app, make sure you have the following installed:

- **Python 3.12.5**: Ensure Python is installed on your machine.
- **SQLAlchemy**: Install using `pip install SQLAlchemy`.
- **alembic**: Install using `pip install alembic`
- **Click**: Install using `pip install Click`.

You will also need a database engine set up (e.g., SQLite, MySQL, or PostgreSQL) and initialized using the SQLAlchemy ORM.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/CGM123sherry/Twende_app
cd twende_app
cd app
```

### 2. Install Dependencies

Make sure you install the required Python dependencies.

```bash
pyenv activate phase3env

pipenv install

pipenv shell
```

### 3. Istall Alembic

````bash
    initialize Alembic:
            alembic init migrations
    ```

    ```bash
        Create a Migration:
                alembic revision -m "Empty Init"
    ```

```bash
        Apply the Migration:
            alembic revision --autogenerate -m "...."
    ```

    ```bash
        To ensure the migrations are up-to-date
            alembic upgrade head
    ```


### 3. Set Up the Database

Before using the app, initialize the database by running:

```bash
python app/cli.py
````

This will create the database tables based on the SQLAlchemy models.

## CLI Commands

The app provides multiple commands to manage passengers, drivers, cabs, and ride requests. Below is a list of available commands with their descriptions:

### 1. Seeding the Database

You can seed the database with predefined data.

```bash
python app/cli.py run-seeds
```

### 2. Assigning a New Driver

To register a new driver in the system:

```bash
python app/cli.py assign-driver
```

You will be prompted for:

- Driver's name
- Driver's email
- Driver's phone number

### 3. Registering a New Cab

You can register a cab by specifying the license number, capacity, and driver ID.

```bash
python app/cli.py register-cab
```

You will be prompted for:

- Cab's license number
- Cab's capacity
- Driver's ID (The driver must already be registered)

### 4. Viewing Ride Requests by a Passenger

To view all ride requests made by a passenger, run the command:

```bash
python app/cli.py location-of-requests
```

You will be prompted for:

- Passenger ID

### 5. Listing All Registered Cabs

To view a list of all registered cabs in the system:

```bash
python app/cli.py list-of-all-registered-cabs
```

### 6. Listing All Registered Drivers

To view a list of all registered drivers:

```bash
python app/cli.py list-of-all-registered-drivers
```

### 7. Deleting a Driver

To delete a driver by their ID:

```bash
python app/cli.py delete-a-driver
```

You will be prompted for:

- Driver's ID

### 8. Deleting a Cab

To delete a cab by its ID:

```bash
python app/cli.py delete-a-cab
```

You will be prompted for:

- Cab's ID

---

## SQLAlchemy Models

The application uses the following models for interacting with the database:

### 1. **Passenger Model**

```python
class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    pickup_location = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    ride_requests = relationship("RideRequest", back_populates="passenger")
```

- Represents passengers who use the cab service.
- Relationships:
  - A passenger can have multiple ride requests.

### 2. **Driver Model**

```python
class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    cab = relationship("Cab", back_populates="driver")
```

- Represents drivers who drive cabs.
- Relationships:
  - One-to-one relationship with a cab.

### 3. **Cab Model**

```python
class Cab(Base):
    __tablename__ = 'cabs'

    id = Column(Integer, primary_key=True)
    license_number = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=False)
    driver = relationship("Driver", back_populates="cab")
    ride_requests = relationship("RideRequest", back_populates="cab")
```

- Represents a cab with a license number and capacity.
- Relationships:
  - One-to-one relationship with a driver.
  - A cab can have multiple ride requests.

### 4. **RideRequest Model**

```python
class RideRequest(Base):
    __tablename__ = 'ride_requests'

    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    passenger_id = Column(Integer, ForeignKey('passengers.id'), nullable=False)
    cab_id = Column(Integer, ForeignKey('cabs.id'), nullable=False)
    passenger = relationship("Passenger", back_populates="ride_requests")
    cab = relationship("Cab", back_populates="ride_requests")
```

- Represents a ride request made by a passenger.
- Relationships:
  - Belongs to a passenger.
  - Belongs to a cab.

---

## Error Handling

Each command is wrapped with `try-except` blocks to handle potential exceptions, such as database errors or invalid user input. Errors are logged using `click.echo()` to provide feedback to the user.

---

### again, the repo is here

## https://github.com/CGM123sherry/Twende_app

please do not forget to

1. cd twende_app
2. cd app

before the virtual env activation, and runing all the other commands.
