from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# Base class for our models to inherit from
Base = declarative_base()

# passenger class
class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    phone_number = Column(String(), nullable=False)
    email = Column(String(), unique=True, nullable=False)
    pickup_location = Column(String(), nullable=False)
    destination = Column(String(), nullable=False)
   
    # one-to-many relationship
    ride_requests = relationship("RideRequest", back_populates="passenger")

    def __repr__(self):
        return f"Passager ID: {self.id}, name: {self.name} phone number: {self.phone_number}" 

# driver class
class Driver(Base):

    __tablename__ = 'drivers'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    email = Column(String(), unique=True, nullable=False)
    phone_number = Column(String(), nullable=False)

    # one-to-one relationship
    cab = relationship("Cab", back_populates="driver")

    def __repr__(self):
        return f"Driver ID: {self.id}, driver name: {self.name}"

# cab class
class Cab(Base):
    __tablename__ = 'cabs'
 
    id = Column(Integer(), primary_key=True)
    license_number = Column(String(), nullable=False)
    capacity = Column(Integer(), default=3, nullable=False)
    driver_id = Column(Integer(), ForeignKey('drivers.id'), nullable=False)

    # one-to-one relationship
    driver = relationship("Driver", back_populates="cab")
    ride_requests = relationship("RideRequest", back_populates="cab")

    def __repr__(self):
        return f"Cab ID: {self.id}, license number: {self.license_number}"

# riderequest class
class RideRequest(Base):
    __tablename__ = 'ride_requests'

    id = Column(Integer(), primary_key=True)
    location = Column(String(), nullable=False)
    passenger_id = Column(Integer(), ForeignKey('passengers.id'), nullable=False)
    cab_id = Column(Integer(), ForeignKey('cabs.id'), nullable=False)

    # one-to-many relationship
    passenger = relationship("Passenger", back_populates="ride_requests")
    cab = relationship("Cab", back_populates="ride_requests")

    def __repr__(self):
        return f"RideRequest ID: {self.id}, location of the request: {self.location}"
