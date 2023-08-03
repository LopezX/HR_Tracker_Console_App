import sqlite3

conn = sqlite3.connect("test.db")

def create(first, last, age):
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS test 
                        (first_name TEXT NOT NULL, 
                        last_name TEXT NOT NULL, 
                        age INTEGER NOT NULL)""")
        
        cursor.execute(f"""INSERT INTO test 
                        VALUES('{first}', '{last}', {age})""")
        
def read(identifiers = None):
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        
        select = "SELECT * FROM test"
        
        if identifiers != None:
            select += " WHERE"
            count = 0
            for identifier in identifiers:
                if identifier == 'First Name':
                    first_name = input("Enter the first name of the person you're searching for: ")
                    select += f" first_name = '{first_name}'"
                if identifier == 'Last Name':
                    last_name = input("Enter the last name of the person you're searching for: ")
                    select += f" last_name = '{last_name}'"
                if identifier == 'Age':
                    age = int(input("Enter the age of the person you're searching for: "))
                    select += f" age = {age}"
                    
                count += 1
                if count < len(identifiers):
                    select += " AND"
        
        # print(select)
        cursor.execute(select)
        
        return cursor.fetchall()
            
def update(old_info, new_info):
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        
        cursor.execute(f"""
                       UPDATE test
                       SET first_name = '{new_info[0]}', 
                       last_name = '{new_info[1]}', 
                       age = {new_info[2]}
                       WHERE first_name = '{old_info[0]}' AND
                       last_name = '{old_info[1]}' AND
                       age = {old_info[2]}
                       """)

def delete(info):
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        
        delete = f"""
        DELETE FROM test
        WHERE first_name = '{info[0]}' AND 
        last_name = '{info[1]}' AND 
        age = {info[2]}"""
        
        cursor.execute(delete)
    

def print_results(results):
    if len(results) > 0:
        print("The person/people we found are: ")
        for data in results:
            first = data[0]
            last = data[1]
            age = data[2]
            print(f"\t{first} {last}, {age} year(s) old")
        print()
    else:
        print("No records were found\n")

def search():
    search = True
    exit_search = False
    info = []
    while search:
        columns = ['First Name', 'Last Name', 'Age']
        length = len(columns)
        identifiers = []
        cont = True
        
        while length > 0 and cont:
            print("What do you want to search by?")
            index = 1
            for column in columns:
                print(f"\t{index} - {column}")
                index += 1
            print("\t0 - Done")
            identifier = input("Selection: ")
            print()
            
            if identifier.isdecimal():
                identifier = int(identifier)
                if identifier < 0 or index <= identifier:
                    print("Invalid selection.\n")
                    identifier = -1
            else:
                print("Invalid selection\n")
                identifier = -1
            
            if identifier == 0:
                cont = False
            elif identifier != -1:
                identifiers.append(columns[identifier - 1])
                columns.pop(identifier - 1)
            
                
            length = len(columns)
        
        if len(identifiers) > 0:
            info = read(identifiers)
        else:
            info = read()
        
        if len(info) == 1:
            print_results(info)
            print("Is this the person you're looking for?")
            choice = input("Y/N: ").upper()
            while choice != 'Y' and choice != 'N':
                print("Invalid choice.\n")
                choice = input("Y/N: ").upper()
            print()
            
            if choice == 'Y':
                info = info[0]
                search = False
            else:
                print("Try a different search?")
                choice = input("Y/N: ").upper()
                while choice != 'Y' and choice != 'N':
                    print("Invalid choice.\n")
                    choice = input("Y/N: ").upper()
                if choice == 'N':
                    search = False
                    exit_search = True
                
        elif len(info) > 1:
            index = 1
            for data in info:
                first = data[0]
                last = data[1]
                age = data[2]
                print(f"{index} - {first} {last}, {age} year(s) old")
                index += 1
            print()
            
            selection = -1
            while selection == -1:
                selection = input("Select the index of the person you're looking for (If none, type 0): ")
                
                if selection.isdecimal():
                    selection = int(selection)
                    if selection < 0 or index <= selection:
                        print("Invalid selection.\n")
                        selection = -1
                else:
                    print("Invalid selection.\n")
                    selection = -1
            print()
            
            if selection == 0:
                print("Try a different search?")
                choice = input("Y/N: ").upper()
                while choice != 'Y' and choice != 'N':
                    print("Invalid choice.\n")
                    choice = input("Y/N: ").upper()
                print()
                
                if choice == 'N':
                    search = False
                    exit_search = True
            else:
                info = info[selection - 1]
                search = False
        
        else:
            print("No candidates found with the filters given.")
            print("Would you like to try with different filters?")
            choice = input("Y/N: ").upper()
            while choice != 'Y' and choice != 'N':
                print("Invalid choice.\n")
                choice = input("Y/N: ").upper()
            print()
            if choice == 'N':
                search = False
                exit_search = True
                
    return [info, exit_search]

option = -1
while option != 0:
    print("1 - create")
    print("2 - read")
    print("3 - update")
    print("4 - delete")
    print("0 - exit program")
    option = input("What option: ")
    print()
    
    if option.isdecimal():
        option = int(option)
        if option < 0 or 4 < option:
            print("Invalid selection.\n\n")
    else:
        print("Invalid selection\n\n")
        option = -1
    
    match option:
        case 1:
            first_name = input("Enter a first name: ")
            last_name = input("Enter a last name: ")
            age = int(input("Enter an age: "))
            print()

            create(first_name, last_name, age)
        case 2:
            columns = ['First Name', 'Last Name', 'Age']
            length = len(columns)
            identifiers = []
            cont = True
            
            while (length > 0) and cont:
                print("What do you want to search by?")
                index = 1
                for column in columns:
                    print(f"\t{index} - {column}")
                    index += 1
                print("\t0 - Done")
                identifier = input("Selection: ")
                print()
                
                if identifier.isdecimal():
                    identifier = int(identifier)
                    if identifier < 0 or index <= identifier:
                        print("Invalid selection.\n")
                        identifier = -1
                else:
                    print("Invalid selection\n")
                    identifier = -1
                
                if identifier == 0:
                    cont = False
                elif identifier != -1:
                    identifiers.append(columns[identifier - 1])
                    columns.pop(identifier - 1)
                
                    
                length = len(columns)
            
            if len(identifiers) > 0:
                info = read(identifiers)
                print_results(info)
            else:
                print("Returning the whole table: \n")
                info = read()
                print_results(info)
        case 3:
            temp = search()
            
            info = temp[0]
            exit_search = temp[1]
            
            if exit_search:
                print("Returning to the main menu.\n")
            else:
                print("The person you are updating is:")
                print(f"First name: {info[0]}")
                print(f"Last name: {info[1]}")
                print(f"Age: {info[2]}")
                print()
                
                columns = ['First Name', 'Last Name', 'Age']
                length = len(columns)
                identifiers = []
                cont = True
                
                while length > 0 and cont:
                    print("What do you want to update?")
                    index = 1
                    for column in columns:
                        print(f"\t{index} - {column}")
                        index += 1
                    print("\t0 - Done")
                    identifier = input("Selection: ")
                    print()
                    
                    if identifier.isdecimal():
                        identifier = int(identifier)
                        if identifier < 0 or index <= identifier:
                            print("Invalid selection.\n")
                            identifier = -1
                    else:
                        print("Invalid selection\n")
                        identifier = -1
                    
                    if identifier == 0:
                        cont = False
                    elif identifier != -1:
                        identifiers.append(columns[identifier - 1])
                        columns.pop(identifier - 1)
                    
                        
                    length = len(columns)
                
                if len(identifiers) > 0:
                    first_name = info[0]
                    last_name = info[1]
                    age = info[2]
                    for identifier in identifiers:
                        if identifier == 'First Name':
                            first_name = input("Enter the new first name: ")
                        if identifier == 'Last Name':
                            last_name = input("Enter the new last name: ")
                        if identifier == 'Age':
                            age = int(input("Enter the new age: "))
                            
                    changes = (first_name, last_name, age)
                            
                    update(info, changes)
                    print("Person's info updated.\n")
                else:
                    print("Nothing updated, returning to main menu.\n")
        case 4:
            temp = search()
            
            info = temp[0]
            exit_search = temp[1]
            
            if not exit_search:
                print("Are you sure you want to delete this person:")
                print(f"{info[0]} {info[1]}, {info[2]} year(s) old\n")
                choice = input("Y/N: ").upper()
                while choice != 'Y' and choice != 'N':
                    print("Invalid choice.\n")
                    choice = input("Y/N: ").upper()
                print()
                
                if choice == 'Y':
                    delete(info)
                    print("Person was deleted.\n")
                else:
                    print("Person not deleted.\n")
