# Create a Python function that takes a list of tuples as an argument.
#Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
#For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:
#"Itinerary 1: Alice - From New York to London
#Itinerary 2: Bob - From Tokyo to San Francisco"

def add_intinerary(flights):
    try:
        name = input("What is your name?: ")
        origin = input("Where are you boarding?: ")
        destination = input("Where will you land?: ")
        flights.append((name, origin, destination))
    except ValueError:
        print("Invalid, please only enter letters.")
def view_intinerary(flights):
    result = []
    for index, (name, origin, destination) in enumerate(flights):
        itin


def main():
    flights = []
    while True:
        print("\n1. Add an itinerary")
        print("\n2. View an itinerary")
        print("\n3. Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            add_intinerary(flights)
        elif choice == "2":
            view_intinerary(flights)
        elif choice == "3":
            print("Thank you, leaving program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()