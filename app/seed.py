# seed.py
from faker import Faker
from db import Session
from models import Passenger, Driver, Cab, RideRequest
import random

# Initialize Faker
fake = Faker()

# seeds the database with sample data
def seed_data():
    # creation of a new session that allows interaction with the database.
    session = Session()

     # Clear existing data to avaoid duplication of data
    session.query(Driver).delete()
    session.query(Cab).delete()
    session.query(Passenger).delete()
    session.query(RideRequest).delete()
    
    # Create drivers and commit
    print("Creating drivers and cabs...")
    
    drivers = [Driver(
        name=fake.name(),
        email=fake.email(),
        phone_number=fake.phone_number()
        )
        for _ in range(20)
        ]
    session.add_all(drivers)
    session.commit()
    

    # Create and commit cabs
    cabs = [Cab(
        
        license_number=fake.license_plate(),
        capacity=3,  
        driver_id=random.choice(drivers).id
        )
        for _ in range(20) 
    ]
    session.add_all(cabs)
    session.commit()  
    
    # Create passengers
    passengers =[ 
        Passenger(
          name= fake.name(),
          phone_number=fake.phone_number(),
          email= fake.email(),
          pickup_location = fake.city(),
          destination= fake.city()

        ) 
        for _ in range(20)]
    session.add_all(passengers)
    session.commit()
    

     # Create ride requests for passengers
    print("Creating ride requests...")

    ride_requests = [RideRequest(location=fake.city(), passenger_id=random.choice(passengers).id,
                                 cab_id=random.choice(cabs).id)
                                 for _ in range (20)
                     ]
    
    session.add_all(ride_requests)
    session.commit()    
    session.close()
    print("Database successfully seeded with fake data!")


# creating the db tables
if __name__ == "__main__":  
    seed_data()
