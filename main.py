#Open the .txt file and write our new contacts, check if the input number is >=0 exp +40xxxxx and if it contains only int
def new_contact():
    f = open("scratch.txt", "a")
    name = input("Name: ")
    number = input("Number: ")
    try:
        int(number)
        if int(number) >= 0:
            f.writelines('{}: {}\n'.format(name, number))
        else:
            print("Invalid phone number ")
    except ValueError:
        print("Invalid phone number ")

def print_contacts():
    contact_list = open("scratch.txt").read()
    print(contact_list)

#Delete 1 entry(drawback is that it deletes the whole .txt in order to replace it with the new formed one)
def delete_entry():
    a_file = open("scratch.txt")
    lines = a_file.readlines()
    for line in lines:
        print(lines.index(line), line)
    del lines[int(input("Entry"))]
    open("scratch.txt", "w").close()
    f = open("scratch.txt", "a")
    f.writelines(lines)

#Delete all data
def clear_phonebook():
    print("You are about to remove ALL contacts")
    yes = input("Erase contacts? Type \'YES\' ").lower()
    if yes == 'yes':
        open('scratch.txt', 'w').close()

def book():
    print("Press 1 to add a new contact ")
    print("Press 2 to see all the contacts ")
    print("Press 3 to ERASE ONE contact ")
    print("Press 4 to ERASE ALL contacts ")
    option = input("Choose your option! ")
    if option == '1':
        new_contact()
    elif option == '2':
        print_contacts()
    elif option == '3':
        delete_entry()
        print("New contact book ")
        print_contacts()
    elif option == '4':
        clear_phonebook()
    else:
        print("Invalid option! ")

book()


