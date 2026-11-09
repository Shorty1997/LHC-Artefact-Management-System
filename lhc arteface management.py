artefacts = []

VALID_CONDITIONS = ["Good", "Damaged", "Under Repair"]


def add_artefact():
    """Add a new artefact to the collection."""
    print("\n--- Add New Artefact ---")

    name = input("Enter artefact name: ").strip()
    if not name:
        print("Error: Artefact name cannot be empty.")
        return

    category = input("Enter artefact category: ").strip()
    if not category:
        print("Error: Artefact category cannot be empty.")
        return

    location = input("Enter artefact location: ").strip()
    if not location:
        print("Error: Artefact location cannot be empty.")
        return

    print("\nAvailable conditions:")
    for condition in VALID_CONDITIONS:
        print("-", condition)

    condition_input = input("Enter artefact condition: ").strip().lower()

    condition = None

    for valid_condition in VALID_CONDITIONS:
        if condition_input == valid_condition.lower():
            condition = valid_condition
            break

    if condition is None:
        print("Error: Invalid condition entered.")
        print("Please use Good, Damaged or Under Repair.")
        return

    new_artefact = {
        "name": name,
        "category": category,
        "location": location,
        "condition": condition
    }

    artefacts.append(new_artefact)

    print("\nArtefact added successfully!")


def update_condition():
    """Update the condition of an existing artefact."""
    print("\n--- Update Artefact Condition ---")

    if not artefacts:
        print("No artefacts are currently recorded.")
        return

    search_name = input("Enter the artefact name: ").strip().lower()

    if not search_name:
        print("Error: Artefact name cannot be empty.")
        return

    for artefact in artefacts:
        if artefact["name"].lower() == search_name:
            print("Current condition:", artefact["condition"])

            print("Available conditions:")
            for condition in VALID_CONDITIONS:
                print("-", condition)

            new_condition_input = input(
                "Enter the new condition: "
            ).strip().lower()

            for valid_condition in VALID_CONDITIONS:
                if new_condition_input == valid_condition.lower():
                    artefact["condition"] = valid_condition
                    print("Artefact condition updated successfully!")
                    return

            print("Error: Invalid condition entered.")
            print("The original condition has not been changed.")
            return

    print("Artefact not found.")


def view_artefacts():
    """Display all artefacts stored in the system."""
    print("\n--- All Artefacts ---")

    if not artefacts:
        print("No artefacts are currently recorded.")
        return

    for number, artefact in enumerate(artefacts, start=1):
        print(f"\nArtefact {number}")
        print("Name:", artefact["name"])
        print("Category:", artefact["category"])
        print("Location:", artefact["location"])
        print("Condition:", artefact["condition"])


def search_artefact():
    """Search for an artefact by its name."""
    print("\n--- Search Artefacts ---")

    if not artefacts:
        print("No artefacts are currently recorded.")
        return

    search_name = input(
        "Enter artefact name to search: "
    ).strip().lower()

    if not search_name:
        print("Error: Search name cannot be empty.")
        return

    found = False

    for artefact in artefacts:
        if artefact["name"].lower() == search_name:
            print("\nArtefact found!")
            print("Name:", artefact["name"])
            print("Category:", artefact["category"])
            print("Location:", artefact["location"])
            print("Condition:", artefact["condition"])
            found = True

    if not found:
        print("No matching artefact was found.")


def main():
    """Display the menu and control the program."""

    while True:
        print("\n================================")
        print(" LHC ARTEFACT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add new artefact")
        print("2. Update artefact condition")
        print("3. View all artefacts")
        print("4. Search for an artefact")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            add_artefact()
        elif choice == "2":
            update_condition()
        elif choice == "3":
            view_artefacts()
        elif choice == "4":
            search_artefact()
        elif choice == "5":
            print("Thank you for using the LHC system.")
            break
        else:
            print("Invalid menu option. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()