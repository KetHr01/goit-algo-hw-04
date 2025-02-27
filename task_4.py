# Парсер команд
def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        return None, None

# Функція, що додає користувача в словник
def add_contact(args, contacts):
    try:
        name, phone = args
        if not isinstance(name, str) or name.isdigit():
            return "Invalid name. It should be a non-numeric text."
        if not phone.isdigit():
            return "Invalid phone number. It should contain only digits."
        if name in contacts:
            return "User already exist."
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid data. There should be name and phone."

# Функція, що змінює номер телефону користувача 
def change_contact(args, contacts):
    try:
        name, phone = args
        if not isinstance(name, str) or name.isdigit():
            return "Invalid name. It should be a non-numeric text."
        if not phone.isdigit():
            return "Invalid phone number. It should contain only digits."
        if name not in contacts:
            return "There is no such user."
        contacts[name] = phone
        return "Contact changed."
    except ValueError:
        return "Invalid data. There should be name and phone."
    
# Функція, що виводить номер телефону користувача
def show_phone(args, contacts):
    try:
        name = args[0].strip()   
        if name not in contacts:
            return "There is no such user."
        return f"{name}: {contacts[name]}"
    except:
        return "Invalid data."

# Функція, що виводить усіх користувачів
def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) 

# Головна функція
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    
