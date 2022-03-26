import os
import sys
from time import sleep
from pick import *
from tabulate import tabulate
import queries as queries

# Terminal interface methods

# Method for handling clearing different output streams for different OSs:
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

# allows user to login, loops if not successful
# prompts user to enter correct input if empty inputs are entered
# informs user of incorrect login-details if either nonexisting user or incorrect password is entered
# returns email and password upon success
def login():
    
    while True:

        email = input('Enter email: ')
        password = input('Enter password: ')
        
        
        if email == '' or password == '':
            print("Invalid input. Please write email or password")
            sleep(0.5)
            continue
        
        db_userdata = queries.get_db_user(email)

        if db_userdata != None:

            if db_userdata[1] == password:
                return email, password

            else:
                print("Incorrect password")
                sleep(1)
                continue

        else:
            print("User not registered in database. Please enter registered user")
            sleep(10)
        
        continue
 
# Would allow user to translate between integer roast-level & roast-level string
# unused           
def translate_to_roast(integer):
    roast_dict = {1:'light', 2: 'medium', 3: 'dark'}
    return roast_dict.get(integer)

# allows user to register one coffee-tasting
# checks if entered coffee is registered in DB before allowing insertion
def add_entry(Epost):
    
    kaffesmaking = {
            'kaffenavn' : '',
            'brennerinavn' : '',
            'poeng' : '',
            'notater' : '',
            'finished' : False
        }
    
    while not kaffesmaking.get('finished'):
        clear()
        
        title = 'Fill in entry details:'
        options = ( 'Kaffenavn: ' + kaffesmaking.get('kaffenavn'),
                    'Brennerinavn: ' + kaffesmaking.get('brennerinavn'),
                    'Poeng: ' + str(kaffesmaking.get('poeng')),
                    'Notater: ' + kaffesmaking.get('notater'),
                    'Finish',
                    'Quit')
        
        selected = pick(options, title)
        
        #print(selected)
        
        #allows user to write in name of coffee
        if selected[0] == 'Kaffenavn: ' + kaffesmaking.get('kaffenavn') :
            kaffesmaking['kaffenavn'] = input("Velg kaffenavn:  ")
        
        #allows user to write in name for roaster
        elif selected[0] == 'Brennerinavn: ' + kaffesmaking.get('brennerinavn') :
            kaffesmaking['brennerinavn'] = input("Velg brennerinavn:  ")
        
        #allows user to assign score to coffe
        elif selected[0] == 'Poeng: ' + str(kaffesmaking.get('poeng')) :
            
            score_title = 'Choose score:'
            score_options = (0,1,2,3,4,5,6,7,8,9,10)
            score_selected = pick(score_options, score_title)
            kaffesmaking['poeng'] = score_selected[0]
        
        #allows user to enter single line of notes
        elif selected[0] == 'Notater: ' + kaffesmaking.get('notater') :
            kaffesmaking['notater'] = input("Skriv notater her:  ")

        #finishes data entry if fields are filled out
        elif selected[0] == 'Finish':
            
            #informs user that they must fill out all fields if they haven't done so
            if (kaffesmaking.get('kaffenavn') == '') or (kaffesmaking.get('brennerinavn') == '') or (kaffesmaking.get('poeng') == ''):
                pick(('Continue',) , 'Missing fields: kaffenavn, brennerinavn, and poeng must be filled out to continue')
                continue
            
            #finishes data entry part of function
            else:
                kaffesmaking['finished'] = True
                continue
            
        #aborts operation, returns to main menu
        elif selected[0] == 'Quit':
            return

    
    # Adds entry to DB, returns true if no error occurred, false otherwise
    success = queries.add_db_entry(Epost, kaffesmaking)
    
    # informs user that entry was added and shows receipt of added item, continues back to main menu
    if success:
        entry_string = str([i[0] + ' : ' + str(i[1]) for i in kaffesmaking.items()])
        entry_added_title = 'Success!\nEntry added to DB\n' + entry_string
        entry_added_option = ('Continue',)
        pick(entry_added_option, entry_added_title)    
        return
    
    # informs user that error occurred, returns to main menu
    else:
        entry_failed_title = 'Error occured, entry not added'
        entry_failed_option = ('Continue',)
        pick(entry_failed_option, entry_failed_title)
        return
                  
# allows user to see a descending list of 50 users who have drunk the most unique coffees
def show_most_unique_coffee_drinkers():
    
    user_data = queries.get_caffeine_addicts()
    
    if user_data != None:
        #print data in a pretty way here
        clear()
        print(tabulate(user_data, headers=["Epost", "Navn", "Antall kaffer smakt"]))
        
        while True:
            try:
                sleep(10)
                continue
            
            except KeyboardInterrupt:
                break
            
        return
        
    else:
        print("error occured, returning to main menu")
        return

# allows user to see a list of 50 coffees with the highest score vs. price sorted descending
def show_value_coffee():
    
    coffee_data = queries.get_value_coffe()
    
    if coffee_data != None:
        #print data in a pretty way here
        clear()
        print(tabulate(coffee_data, headers=["Brennerinavn","Kaffenavn", "Kilopris", "Gjennomsnitt Poeng", "Poeng per 100KR"]))
        
        while True:
            try:
                sleep(10)
                continue
            
            except KeyboardInterrupt:
                break
            
        return
        
    else:
        print("error occured, returning to main menu")
        return

# allows user to enter a string to search coffees with a description (user-generated or written by roaster) that matches the string
def search_for_description():

    clear()
    description = input('Which description are you looking for:    ')
    matching_coffees = queries.search_db_for_descripton(description)
    
    if matching_coffees != None:
        #print data in a pretty way here
        clear()
        print(tabulate(matching_coffees, headers=["Brennerinavn","Kaffenavn"]))
        
        while True:
            try:
                sleep(10)
                continue
            
            except KeyboardInterrupt:
                break
        
        return
        
    else:
        print("error occured or no matching coffee was found, returning to main menu")
        sleep(1)
        return

# allows users to find coffees according to their choice of processes and countries of origin
def country_process_search():
    
    processes = queries.get_processes()
    countries = queries.get_countries()
    
    search_process_tuple = pick(processes, 'Choose which processes to search for:', multiselect=True, min_selection_count=1)
    search_countries_tuple = pick(countries, 'Choose which countries to search for:', multiselect=True, min_selection_count=1)
    
    coffee_data = queries.country_process_search(search_process_tuple, search_countries_tuple)
    
    if coffee_data != None:
        #print data in a pretty way here
        clear()
        print(tabulate(coffee_data, headers=["Brennerinavn","Kaffenavn"]))
        
        while True:
            try:
                sleep(10)
                continue
            
            except KeyboardInterrupt:
                break
            
        return
        
    else:
        print("error occured, returning to main menu")
        return

# main method
# takes email and password to ensure user is logged in and to store proper creditentals in DB
# password goes unused
def main(email, password):
    
    while True:
        title = 'Choose which operation you want to do:'
        options = ('Add entry', 'Show users who\'ve tasted the most unique coffees', 'Show coffee with most bang for your buck', 'Search for description', 'Search for coffees by process & country of origin', 'Quit')
        selected = pick(options, title)
        print(selected)
        
        #Allows user to add coffee-tasting to DB
        if selected[0] == 'Add entry':
            add_entry(email)
            
            
        elif selected[0] == 'Show users who\'ve tasted the most unique coffees':
            show_most_unique_coffee_drinkers()
            
            
        elif selected[0] == 'Show coffee with most bang for your buck':
            show_value_coffee()
            
            
        elif selected[0] == 'Search for description':
            search_for_description()
         
            
        elif selected[0] == 'Search for coffees by process & country of origin':
            country_process_search()
         
            
        elif selected[0] == 'Quit':
            email = None
            password = None
            clear()
            print('Goodbye!') 
            sleep(1)
            quit()
        
        
        else:
            print('Invalid operation (also, how did you get here?)')

# Program runs here:
email, password = login()
main(email, password)