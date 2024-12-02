def add_itinerary(flights):
    try:
        name = input("What is your name?: ")
        if not name.isalpha():
            print("Invalid input! Name should only contain letters.")
            return
        
        origin = input("Where are you boarding?: ")
        if not origin.isalpha():
            print("Invalid input! Origin should only contain letters.")
            return
        
        destination = input("Where will you land?: ")
        if not destination.isalpha():
            print("Invalid input! Destination should only contain letters.")
            return
        
        flights.append((name, origin, destination))
        print("Itinerary added successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def view_itinerary(flights):
    if not flights:
        print("No itineraries available.")
        return
    
    result = []
    for index, (name, origin, destination) in enumerate(flights):
        itinerary = f"Itinerary {index + 1}: {name} - From {origin} to {destination}"
        result.append(itinerary)
    
    print("\n".join(result))

def main():
    flights = []
    while True:
        print("\n1. Add an itinerary")
        print("2. View itineraries")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_itinerary(flights)
        elif choice == "2":
            view_itinerary(flights)
        elif choice == "3":
            print("Thank you, leaving program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
