# # app/cli.py

from models import Passenger, Driver, Cab, RideRequest
from db import Session

# Display a welcome message
def welcome_message():
    print("\n")
    print("***********************************")
    print( "**Welcome to TWENDE Cab System")
    print("***********************************")
    print("Manage passengers, drivers, cabs, and ride requests easily.")
    print("To navigate, please follow the instructions!")
    print("\n")


# Main menu for the user
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Passenger Menu")
        print("2. Driver Menu")
        print("3. Cab Menu")
        print("4. Ride Request Menu")
        print("5. Exit")

        choice = input("Choose an option: ")
        # loops indefinitly while waiting for the user input
        if choice == '1':
            model_menu(Passenger, "Passenger")
        elif choice == '2':
            model_menu(Driver, "Driver")
        elif choice == '3':
            model_menu(Cab, "Cab")
        elif choice == '4':
            model_menu(RideRequest, "Ride Request")
        elif choice == '5':
            exit_program()
        else:
            print("Invalid option, please try again.")

# modeling the menu
def model_menu(model, model_name):
    while True:
        print(f"\n--- {model_name} Menu ---")
        print(f"1. Create {model_name}")
        print(f"2. View All {model_name}s")
        print(f"3. Find {model_name} by ID")
        print(f"4. Delete {model_name}")
        print("5. Back to Main Menu")

        choice = input(f"Choose an option for {model_name}: ")
        if choice == '1':
            create_object(model, model_name)
        elif choice == '2':
            list_objects(model, model_name)
        elif choice == '3':
            find_object_by_id(model, model_name)
        elif choice == '4':
            delete_object(model, model_name)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

# Create object for any model
def create_object(model, model_name):
    session = Session()
    try:
        # builds a dict, that excludes an id
        fields = {column.name: input(f"Enter {model_name} {column.name}: ") 
                  for column in model.__table__.columns if column.name != 'id'}
        obj = model(**fields)
        session.add(obj)
        session.commit()
        print(f"{model_name} created successfully.")
        # prints an error incase there's one
    except Exception as e:
        print(f"Error creating {model_name}: ", e)
    finally:
        session.close()

# List all objects of a given model
def list_objects(model, model_name):
    session = Session()
    try:
        # retrieves all records of the model
        objects = session.query(model).all()
        if objects:
            for obj in objects:
                print(obj)
        else:
            print(f"No {model_name}s found.")
            # prints an error incase there's no record
    except Exception as e:
        print(f"Error listing {model_name}s: ", e)
    finally:
        session.close()

# Find object by ID for any model
def find_object_by_id(model, model_name):
    session = Session()
    obj_id = input(f"Enter {model_name} ID: ")
    try:
        # retrieves the given model
        obj = session.query(model).get(obj_id)
        if obj:
            print(obj)
        else:
            print(f"No {model_name} found with ID {obj_id}.")
             # prints an error incase there's no record
    except Exception as e:
        print(f"Error finding {model_name}: ", e)
    finally:
        session.close()

#Delete object by ID for any model
def delete_object(model, model_name):
    session = Session()
    obj_id = input(f"Enter {model_name} ID to delete: ")
    try:
      
        obj = session.query(model).get(obj_id)
        if obj:
            session.delete(obj)
            session.commit()
            print(f"{model_name} deleted successfully.")
        else:
            print(f"No {model_name} found with ID {obj_id}.")
    except Exception as e:
        print(f"Error deleting {model_name}: ", e)
    finally:
        session.close()

#Exit program
def exit_program():
    print("Exiting...")
    exit()

if __name__ == "__main__":
    main_menu()

