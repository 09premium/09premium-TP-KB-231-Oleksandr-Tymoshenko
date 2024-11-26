# already sorted list
list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "address": "123 Elm St"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "address": "456 Oak St"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@example.com", "address": "789 Pine St"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@example.com", "address": "101 Maple St"}
]

def printAllList():
    for elem in list:
        print(f"Student name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Address: {elem['address']}")
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    newItem = {"name": name, "phone": phone, "email": email, "address": address}
    # Find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print(f"Element '{name}' has been deleted")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    for item in list:
        if name == item["name"]:
            print(f"Current data: {item}")
            new_phone = input(f"Enter new phone (current: {item['phone']}): ") or item['phone']
            new_email = input(f"Enter new email (current: {item['email']}): ") or item['email']
            new_address = input(f"Enter new address (current: {item['address']}): ") or item['address']
            # Update item
            item["phone"] = new_phone
            item["email"] = new_email
            item["address"] = new_address
            # Re-sort list
            list.sort(key=lambda x: x["name"])
            print("Student data has been updated")
            return
    print("Student not found")
    return

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted:")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed:")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()
