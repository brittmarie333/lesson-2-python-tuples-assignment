# Create a Python function that takes a list of tuples as an argument.
#Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
#For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:
#"Itinerary 1: Alice - From New York to London
#Itinerary 2: Bob - From Tokyo to San Francisco"



def main():
    options = []
    while True:
        print("\n1. Add an itinerary")
        print("\n2. View an itinerary")
        print("\n3. Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            add_itinerary()