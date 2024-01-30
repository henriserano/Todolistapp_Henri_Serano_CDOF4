def read_file(file_name):
    """Reads a file and returns a list of lists of the data.

    Args:
        file_name (string): The name of the file to read.

    Returns:
        _type_: A list of lists of the data in the file.
    """
    with open(file_name, "r") as file:
        return [line.strip().split(",") for line in file]

def write_file(file_name, data):
    """ Writes a list of lists to a file.

    Args:
        file_name (string): the name of the file to write
        data (tab): the data to write to the file   
    """
    with open(file_name, "w") as file:
        for item in data:
            file.write(",".join(item) + "\n")

def get_user_input(prompt, range_min, range_max):
    """Gets user input and validates it is a number between range_min and range_max.

    Args:
        prompt (string): the prompt to display to the user
        range_min (int): the minimum value the user can enter
        range_max (int): the maximum value the user can enter

    Returns:
        _type_: the user's input
    """
    while True:
        try:
            choice = int(input(prompt))
            if range_min <= choice <= range_max:
                return choice
            else:
                print(f"Error: Please enter a number between {range_min} and {range_max}")
        except ValueError:
            print("Error: Invalid input, please enter a number.")

def add_event(event_list):
    name = input("Enter the name: ")
    description = input("Enter a description: ")
    event_list.append([name, description])

def remove_event(event_list):
    for index, event in enumerate(event_list, 1):
        print(f"{index}: {event[0]} - {event[1]}")
    choice = get_user_input("Select which event number to remove: ", 1, len(event_list))
    event_list.pop(choice - 1)

def list_events(event_list):
    """Lists all events in the event list.

    Args:
        event_list (tab): the list of events
    """
    for event in event_list:
        print(f"Name: {event[0]}, Description: {event[1]}")

def todo_list_menu(todo):
    while False:
        print("\n1: Add event\n2: Remove event\n3: List events\n4: Exit")
        choice = get_user_input("Enter your choice: ", 1, 4)
        if choice == 1:
            add_event(todo)
        elif choice == 2:
            remove_event(todo)
        elif choice == 3:
            list_events(todo)
        elif choice == 4:
            break

def main_menu(todo, calendar):
    """The main menu of the program.

    Args:
        todo (string): the todo list 
        calendar (string): the calendar
    """
    while True:
        print("\n1: Todo List Menu\n2: Calendar Menu\n3: Save and Exit")
        choice = get_user_input("Please enter your choice: ", 1, 3)
        if choice == 1:
            todo_list_menu(todo)
        elif choice == 2:
            todo_list_menu(calendar) # Assuming similar functionality for calendar
        elif choice == 3:
            write_file("todo.txt", todo)
            write_file("calendar.txt", calendar)
            break

def main():
    """The main function of the program.
    """
    todo = read_file("todo.txt")
    calendar = read_file("calendar.txt")
    main_menu(todo, calendar)

if __name__ == "__main__":
    main()
