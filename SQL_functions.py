import sqlite3
from validation import *

def create_candidate_entry(id, first_name, last_name, email, 
                           phone_number = None, profiles = None):
    #connect to database
        #create a connection
    with sqlite3.connect('hr_candidates.db') as conn:
        #create a cursor
        cursor = conn.cursor()
        
        #create table, if one does not exist
        cursor.execute("""CREATE TABLE IF NOT EXISTS candidates 
                          (candidate_id INTEGER UNIQUE NOT NULL, 
                          first_name TEXT NOT NULL, 
                          last_name TEXT NOT NULL, 
                          email TEXT NOT NULL, 
                          phone_number TEXT, 
                          profiles TEXT)""")
        
        #create and insert statement
        create_candidate = f"""INSERT INTO candidates VALUES 
                               ({id}, 
                               '{first_name}', 
                               '{last_name}', 
                               '{email}', 
                               '{phone_number}', 
                               '{profiles}')"""
        #execute insert statement
        try:
            cursor.execute(create_candidate)
        except sqlite3.IntegrityError:
            print("Candidate ID already exists.")
            print("Would you like to update the candidate instead?")

def search_candidate_entry(candidate_indentifiers = []):
    #To check that profiles match
    profile_check = False
    
    #connect to database
        #create a connection
    with sqlite3.connect('hr_candidates.db') as conn:
        #create a cursor
        cursor = conn.cursor()
    #select candidate based on identifier
        #create a select statement
        select = "SELECT * FROM candidates"
        
        #add filters to find candidate(s)
        if len(candidate_indentifiers) > 0:
            filters = []
            count = 0
            for filter in candidate_indentifiers:
                if filter == "Candidate ID":
                    id = valid_id()
                    filters.append(f" candidate_id = {id}")
                if filter == "First Name":
                    first_name = valid_first_name()
                    filters.append(f" first_name = '{first_name}'")
                if filter == "Last Name":
                    last_name = valid_last_name()
                    filters.append(f" last_name = '{last_name}'")
                if filter == "Email":
                    email = valid_email()
                    filters.append(f" email = '{email}'")
                if filter == "Phone Number": 
                    phone_number = valid_phone_number()
                    filters.append(f" phone_number = '{phone_number}'")
                if filter == "Profiles":
                    profile_check = True
                    count -= 1
                    
                count += 1
            
            if len(filters) > 0:
                select += " WHERE"
                for filter in filters:
                    select += filter
                    if 1 < count:
                        count -= 1
                        select += " AND"
                
        select += " ORDER BY candidate_id ASC"
        
        #execute select statement
        cursor.execute(select)
        
    #return query results
        #store the results of the select statement
        results = cursor.fetchall()
        
        if profile_check:
            profile_comparisons = valid_profiles()
            while profile_comparisons == None:
                print("You selected to filter by profiles.")
                print("Please type what profiles the candidate(s) you're looking for are on.")
                profile_comparisons = valid_profiles()
            
            final_results = []
            for result in results:
                profiles = result[5].split()
                profiles_to_compare = profile_comparisons.split()
                profile_found = False
                
                for profile in profiles:
                    for comparison in profiles_to_compare:
                        if profile.lower() == comparison.lower():
                            profile_found = True
                            
                if profile_found:
                    final_results.append(result)
            
            results = final_results
                    
        return results
    

def update_candidate_entry(old_info, new_info):
    #connect to database
        #create a connection
    with sqlite3.connect("hr_candidates.db") as conn:
        #create a cursor
        cursor = conn.cursor()
        
    #update the candidate's information with the information_needed and
    #return the candidate back to the query
        #create an update statement
        update = "UPDATE candidates SET "
        
        #Set new information
        update += f"candidate_id = {new_info[0]}, "
        update += f"first_name = '{new_info[1]}', "
        update += f"last_name = '{new_info[2]}', "
        update += f"email = '{new_info[3]}', "
        update += f"phone_number = '{new_info[4]}', "
        update += f"profiles = '{new_info[5]}' "
        
        #Replace old information
        update += "WHERE "
        update += f"candidate_id = {old_info[0]} AND "
        update += f"first_name = '{old_info[1]}' AND "
        update += f"last_name = '{old_info[2]}' AND "
        update += f"email = '{old_info[3]}' AND "
        update += f"phone_number = '{old_info[4]}' AND "
        update += f"profiles = '{old_info[5]}'"
        #execute update statement
        cursor.execute(update)

def delete_candidate_entry(info):
    #connect to database
        #create a connection
    with sqlite3.connect("hr_candidates.db") as conn:
        #create a cursor
        cursor = conn.cursor()

    #select candidate based on identifier and remove candidate from the database
        #create a delete statement
        delete = "DELETE FROM candidates WHERE "
        delete += f"candidate_id = {info[0]} AND "
        delete += f"first_name = '{info[1]}' AND "
        delete += f"last_name = '{info[2]}' AND "
        delete += f"email = '{info[3]}' AND "
        delete += f"phone_number = '{info[4]}' AND "
        delete += f"profiles = '{info[5]}'"
        #execute delete statement
        
        cursor.execute(delete)