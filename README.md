# HR_Tracker_Console_App
My first self-developed Python Console App

This app will allow a user to create, read, edit, and delete potential candidates they are looking to hire. The app provides a simple and easy to understand format that navigates the user through the main menu to their desired option. These include:

# Create Candidate:
Adds the user's potential candidate to your database. The candidate's ID, first name, last name, and email are required to enter. There are two optional fields, phone number and profiles (such as LinkedIn, Indeed, etc.). Each field that is completed will have their own verification call, ensuring that every ID, name, email, phone number, and profiles match their respective rules so that 1) it can be stored in the database correctly, and 2) there are no illegal names, emails, etc. Once the information has been filled out, it will save the Candidate's information to the user's database.

# Read Candidates:
Search for a candidate given any or no filters. If the user want to view the whole table, simply don't use any filters, and the app will print to the screen all of the candidates in the database. If you're looking for a specific candidate, then add the filters and, if there is a candidate that matches all of the filters, the app will display only those candidates. If none match your filter, no candidates will be displayed.

# Edit Candidate:
Edit a candidate entry. Only one candidate can be updated at a time. First, the candidate the user is trying to update will be searched through filters (if no filters are provided, then the entire candidate database will be returned). If multiple candidates are found with the given filters, then the user will decide which candidate to update. If the desired candidate wasn't found, then the user can try again or not edit any candidate at all. Once a candidate is chosen, the app will ask the user what information they would like to update. Once those option or options are selected, the user will then enter the new values, with the app verifying they are valid inputs. Once completed, the candidate's information will be updated, and it can be seen when viewing that candidate.

# Delete Candidate:
Delete a candidate entry. Only one candidate can be deleted at a time. First, the user will search for the candidate they are trying to delete through searching with filters. If no candidates are found, the user can try again, if they wish. If multiple candidates are found, the user will choose which user to delete, try another search with different filters, or not delete any candidate. Once a candidate is selected, the app will ask if the user is sure on deleting the candidate. If they say yes, the candidate is deleted from the database. If the user says no, nothing will change in the database.

# How to run
To run this application, first these 3 imports must be installed and connected to your Python Path:
- re
- email_validator
- sqlite3
Once installed, run the "HR_Tracker.py" in your Command Prompt with the following command:

python HR_Tracker.py

This will open the application. There is sample data provided that can be used to practice the functionality. Hope you enjoy this simple app!
