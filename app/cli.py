# # app/cli.py

from models import Passenger, Driver, Cab, RideRequest
from db import Session, init_db
from seed import seed_data as seed_all
import click 

@click.group()
def cli():
    """Twende cab managemnet system"""
    pass

# seeding the db
@cli.command(help="seed the database")
def run_seeds():
    """Seed the database"""
    session=Session()
    try: 
        click.echo("seeding the database")
        seed_all()
        click.echo("seeding is complete")
    except Exception as e:
        click.echo(f"error occurred: {e}")
    finally:
        session.close()

# assigning a new driver
@cli.command()
@click.option("--name",prompt="Driver name", help="Name of the driver")
@click.option("--email",prompt="Driver's email", help="Email of the driver")
@click.option("--phone_number",prompt="Driver's phone number(+254)", help="Phone number of the driver")
def assign_driver(name, email, phone_number):
    """Assign a new driver"""
    session=Session()
    try:
        driver=Driver(name=name, email=email, phone_number=phone_number)
        session.add(driver)
        session.commit()
        click.echo(f"{driver.name} is the new driver")
    except Exception as e:
        click.echo(f"error occurred: {e}")
    finally:
        session.close()

# register a new cab
@cli.command()
@click.option("--license_number",prompt="Cab license number", help="License number of the cab")
@click.option("--capacity",prompt="Cab's capacity", help="Capacity of the cab")
@click.option("--driver_id", prompt="Driver's id", type=int, help="ID of the driver")
def register_cab(license_number, capacity, driver_id):
    """register a new cab"""
    session=Session()
    try:
        cab=Cab(license_number=license_number.upper(),capacity=capacity, driver_id=driver_id)
        session.add(cab)
        session.commit()
        click.echo(f"New cab with plate number {cab.license_number.upper()} registered")
    except Exception as e:
        click.echo(f"error occurred: {e}")
    finally:
        session.close()
    

# location of requests made by a passenger
@cli.command()
@click.option("--passanger_id",prompt="Passager's id", type=int, help="ID of the passanger")
def location_of_requests(passenger_id):
    """Location of requests made by a passenger"""
    session=Session()
    try:
        requests=session.query(RideRequest).filter(RideRequest.passenger_id==passenger_id).all()
        if requests:
            click.echo(f"Location of requests made by passenger {passenger_id}: ")
            for request in requests:
                click.echo(f" -{request.location}")
        else:
            click.echo(f"no request made by passenger {passenger_id}")
    except Exception as e:
        click.echo(f"Error occurred: {e}")
        return None
    finally:
        session.close()

# list of all registered cabs
@cli.command()
def list_of_all_registred_cabs():
    """A list of all the registered cabs"""
    session=Session()
    try:
        all_registred_cabs=session.query(Cab).all()
        if all_registred_cabs:
            click.echo(f"License number plate of registered cabs")
            for cab in all_registred_cabs:
                click.echo(f"{cab}")
        else:
            click.echo(f"No registered cabs!")
    except Exception as e:
        click.echo(f"Error occurred: {e}")
        return None
    finally:
        session.close()

# list of all registered drivers
@cli.command()
def list_of_all_registred_drivers():
    """A list of all the registered drivers"""
    session=Session()
    try:
        all_registred_drivers=session.query(Driver).all()
        if all_registred_drivers:
            click.echo(f"Names of registered drivers")
            for driver in all_registred_drivers:
                click.echo(f"{driver}")
        else:
            click.echo(f"No registered drivers!")
    except Exception as e:
        click.echo(f"Error occurred: {e}")
        return None
    finally:
        session.close()


#deleting a driver
@cli.command()
@click.option("--driver_id",prompt="Driver's id", type=int, help="ID of the driver")
def delete_a_driver(driver_id):
    """Delete a registered driver"""
    session=Session()
    try:
        driver_to_delete=session.query(Driver).filter(Driver.id==driver_id).first()
        if driver_to_delete:
            driver_name=driver_to_delete.name
            session.delete(driver_to_delete)
            session.commit()
            click.echo(f"Driver with id: {driver_id}, {driver_name} deleted successfully!")
        else:
            click.echo(f"no driver found with id: {driver_id}!")
    except Exception as e:
        click.echo(f"Error occurred: {e}")
        return None
    finally:
        session.close() 


#deleting a cab
@cli.command()
@click.option("--cab_id",prompt="Cab's id", type=int, help="ID of the cab")
def delete_a_cab(cab_id):
    """Delete a registered cab"""
    session=Session()
    try:
        cab_to_delete=session.query(Cab).filter(Cab.id==cab_id).first()
        if cab_to_delete:
            cab_license_number=cab_to_delete.license_number
            session.delete(cab_to_delete)
            session.commit()
            click.echo(f"Cab with id: {cab_id}, {cab_license_number} deleted successfully!")
        else:
            click.echo(f"No cab found with id: {cab_id}!")
    except Exception as e:
        click.echo(f"Error occurred: {e}")
        return None
    finally:
        session.close() 

               

if __name__ == "__main__":
    init_db()
    cli()

    # run_seeds()
    # assign_driver("sheila", "edc@ghu.com", "070202988756")
    # register_cab("dsfgbi", "2", "12")
    # location_of_requests_by_passenger(16)
    # list_of_all_registred_cabs()
    # list_of_all_registred_drivers()
    # delete_a_driver(21)
    # delete_a_cab(21)


