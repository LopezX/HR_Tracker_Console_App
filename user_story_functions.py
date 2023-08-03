from SQL_functions import *

def read_candidates_print(results):    
    if len(results) > 0:
        print("Candidates that matched your filters:\n")
        print("Row       |" +
          "ID        |" +
          "First Name          |" +
          "Last name                     |" +
          "Email                                   |" +
          "Phone Number   |" +
          "Profiles                           ")
        print("-" * 155)
        row = 1
        for result in results:
            id = result[0]
            first_name = result[1]
            last_name = result[2]
            email = result[3]
            phone_number = result[4]
            profiles = result[5]
            
            info = str(row)
            offset = 10 - len(str(row))
            info += ' ' * offset + '|'
            
            info += str(id)
            offset = 10 - len(str(id))
            info += ' ' * offset + '|'
            
            info += first_name
            offset = 20 - len(first_name)
            info += ' ' * offset + '|'
            
            info += last_name
            offset = 30 - len(last_name)
            info += ' ' * offset + '|'
            
            info += email
            offset = 40 - len(email)
            info += ' ' * offset + '|'
            
            info += phone_number
            offset = 15 - len(phone_number)
            info += ' ' * offset + '|'
            
            info += profiles
            offset = 35 - len(profiles)
            info += ' ' * offset
            
            print(info)
            row += 1
        print()
    else:
        print("No results matched your filters.\n")
        
def get_filters():
    columns = ["Candidate ID" , "First Name", "Last Name", 
                       "Email", "Phone Number", "Profiles"]
    length = len(columns)
    filters = []
    cont = True
    
    #Get the filters being used
    while length > 0 and cont:
        #Print all unused filters
        print("Select a filter to find candidate(s):")
        index = 1
        for column in columns:
            print(f"\t{index} - {column}")
            index += 1
        print("\t0 - Done/No Filters")
        #Get a filter selection
        selection = input("Selection: ")
        print()
        
        if selection.isdecimal():
            selection = int(selection)
            if selection < 0 or index <= selection:
                print("Invalid selection.\n")
                selection = -1
        else:
            print("Invalid selection\n")
            selection = -1
        
        if selection == 0:
            cont = False
        elif selection != -1:
        #Add filter selection
            filters.append(columns[selection - 1])
            columns.pop(selection - 1)
            
        length = len(columns)
    
    return filters

def get_verification():
    choice = input("Y/N: ").upper()
    while choice != 'Y' and choice != 'N':
        print("Invalid choice.\n")
        choice = input("Y/N: ").upper()
    print()
    
    return choice

def search():
    search = True
    exit_search = False
    results = []
    
    while search:
    #Select filters to find candidate
        filters = get_filters()
        
        #If no filters, ask if they want to view the whole table
        if len(filters) == 0:
            print("Do you want to view the entire table?")
            choice = get_verification()
            
            #If yes, print the whole table
            if choice == 'Y':
                search = False
                results = search_candidate_entry()
                read_candidates_print(results)
                
                #Ask which candidate to update
                print(f"There are {len(results)} candidate(s).")
                selection = -1
                while selection == -1:
                    selection = input("Select the row of the candidate you want to update (0 if none): ")
                    if selection.isdecimal():
                        selection = int(selection)
                        if selection < 0 or len(results) < selection:
                            selection = -1
                            print("Invalid row.\n")
                    else:
                        selection = -1
                        print("Invalid row.\n")
                print()
                
                #If no candidate selected, return to main menu
                if selection == 0:
                    print("No candidate was selected from the entire table.")
                    print("Returning to main menu.\n")
                    exit_search = True
                #If candidate was selected, hold onto that info
                else:
                    results = results[selection - 1]
                
            #If no, ask if the user wants to continue searching
            else:
                print("Want to keep searching for candidate to update?")
                choice = get_verification()
                
                #If not, exit to the main menu
                if choice == 'N':
                    print("Returning to main menu.\n")
                    search = False
                    exit_search = True
        else:
            results = search_candidate_entry(filters)
            
            #If no results were found from the given filters, ask to try again
            if len(results) == 0:
                print("No results were found with the filters given.")
                print("Try again?")
                choice = get_verification()
                
                #If not, exit to main menu
                if choice == 'N':
                    print("Returning to the main menu\n")
                    search = False
                    exit_search = True
            #If one result was found, ask if its the correct candidate
            elif len(results) == 1:
                read_candidates_print(results)
                print("Is this the candidate you're looking for?")
                choice = get_verification()
                
                #If so, hold onto that info
                if choice == 'Y':
                    search = False
                    results = results[0]
                #If not, ask if they would like to search again
                else:
                    print("Would you like to search again?")
                    choice = get_verification()
                    
                    #If not, exit to main menu
                    if choice == 'N':
                        print("Returning to main menu.\n")
                        search = False
                        exit_search = True
            #If multiple results were found
            else:
                read_candidates_print(results)
                print(f"There are {len(results)} candidates that matched the filters.")
                selection = -1
                while selection == -1:
                    selection = input("Select the row of the candidate you want to update (0 if none): ")
                    if selection.isdecimal():
                        selection = int(selection)
                        if selection < 0 or len(results) < selection:
                            selection = -1
                            print("Invalid row.\n")
                    else:
                        selection = -1
                        print("Invalid row.\n")
                print()
                
                #If no candidate selected, ask if they would like to do another search
                if selection == 0:
                    print("No candidate was selected.")
                    print("Would you like to try a different search?")
                    choice = get_verification()
                    
                    if choice == 'N':
                        print("Returning to main menu.\n")
                        search = False
                        exit_search = True
                #If candidate was selected, hold onto that info
                else:
                    results = results[selection - 1]
                    search = False
    
    return [results, exit_search]

print("Hello! Welcome to Thomas Instrument's HR Tracker!\n\n")
option = -1
while (option != 0):
    print("Please select one of the following options:\n")
    print("\t1 - Create a candidate entry")
    print("\t2 - Read a candidate entry")
    print("\t3 - Update a candidate entry")
    print("\t4 - Delete a candidate entry")
    print("\t0 - Exit HR Tracker")
    print()
    option = input("Enter your option: ")
    
    if option.isdecimal():
        option = int(option)
        if option < 0 or 4 < option:
            print("Invalid selection.\n\n")
    else:
        print("Invalid selection\n\n")
        option = -1
    print()
    
    match option:
        case 1:
        #Get Candidate Info
            print("\n\n-------------------------------------------------------")
            print("Please enter the following information for the new candidate:\n")
            
            #Get Candidate ID
            id = valid_id()
            #Get Candidate's first name
            first_name = valid_first_name()
            #Get Candidate's last name
            last_name = valid_last_name()
            #Get Candidate's email
            email = valid_email()
            #Get Candidate's phone-number (if applicable)
            phone_number = valid_phone_number()
            #Get Candidate's profiles (LinkedIn, Indeed, etc.) (if applicable)
            profiles = valid_profiles()
            
            #Create candidate entry
            create_candidate_entry(id, first_name, last_name, email, phone_number, profiles)
        case 2:
            filters = get_filters()
            
        #Print filtered results
            if len(filters) > 0:
                results = search_candidate_entry(filters)
                read_candidates_print(results)
            #If no filters given, ask for user if they want the whole table
            else:
                print("Do you want to see the entire table of current candidates?")
                choice = get_verification()
                
                if choice.upper() == 'Y':
                    results = search_candidate_entry()
                    read_candidates_print(results)
                else:
                    print("Nothing will be printed, returning to the main menu.\n")
        case 3:
        #Find the candidate to update
            find = search()
            
            results = find[0]
            exit_search = find[1]
                        
            if not exit_search:
            #Get information to update
                columns = ["Candidate ID" , "First Name", "Last Name", 
                       "Email", "Phone Number", "Profiles"]
                length = len(columns)
                columns_to_update = []
                cont = True
                
                #Select what needs to be updated
                while length > 0 and cont:
                    #Print all unused filters
                    print("What do you want to update:")
                    index = 1
                    for column in columns:
                        print(f"\t{index} - {column}")
                        index += 1
                    print("\t0 - Done/No Filters")
                    #Get a filter selection
                    selection = input("Selection: ")
                    print()
                    
                    if selection.isdecimal():
                        selection = int(selection)
                        if selection < 0 or index <= selection:
                            print("Invalid selection.\n")
                            selection = -1
                    else:
                        print("Invalid selection\n")
                        selection = -1
                    
                    if selection == 0:
                        cont = False
                    elif selection != -1:
                    #Add filter selection
                        columns_to_update.append(columns[selection - 1])
                        columns.pop(selection - 1)
                        
                    length = len(columns)
                
                #If no columns given, exit to main menu
                if len(columns_to_update) == 0:
                    print("Nothing to update, returning to main menu.\n")
                #Get the updated information
                else:
                    id = results[0]
                    first_name = results[1]
                    last_name = results[2]
                    email = results[3]
                    phone_number = results[4]
                    profiles = results[5]
                    
                    for column in columns_to_update:
                        if column == 'Candidate ID':
                            id = valid_id()
                        if column == 'First Name':
                            first_name = valid_first_name()
                        if column == 'Last Name':
                            last_name = valid_last_name()
                        if column == 'Email':
                            email = valid_email()
                        if column == 'Phone Number':
                            phone_number = valid_phone_number()
                        if column == 'Profiles':
                            profiles = valid_profiles()
                
                    #Update information
                    changes = (id, first_name, last_name, email, phone_number, profiles)
                    
                    update_candidate_entry(results, changes)
                    
                    print("Candidate was updated.\n")
        case 4:
            #Find candidate to delete
            find = search()
            
            results = find[0]
            exit_search = find[1]
            #Verify that they want to delete candidate
            if not exit_search:
                print("Are you sure you want to delete the following candidate:\n")
                print(f"ID: {results[0]}")
                print(f"Name: {results[1]} {results[2]}")
                print(f"Email: {results[3]}")
                print(f"Phone Number: {results[4]}")
                print(f"Profiles: {results[5]}")
                print()
                choice = get_verification()
                
                if choice == 'Y':
                    #Delete candidate
                    delete_candidate_entry(results)
                    print("Candidate was removed from the database.\n")

print()
print("Thank you for using Thomas Instrument HR Tracker.")
print("Have a great rest of your day!")
print()
print("Exiting program...")
