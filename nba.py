#docstring - Jack Bai - NBA player database application
#imports
import sqlite3

#variables
database = 'player.db'

#functions
#prints all players
def print_all_players():
    '''print all the data nicely'''
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM player;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                      Points Per Game   Usage rate (%)   Points Created")
    for stats in results:
        print(f"{stats[0]:<26}{stats[3]:<18}{stats[4]:<17}{stats[5]}")
    #loop finish here
    db.close()  

#prints ppg
def print_points_per_game():
    '''print all the data nicely'''
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM player WHERE ppg ORDER BY ppg DESC;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                      Points Per Game   Usage rate (%)   Points Created")
    for stats in results:
        print(f"{stats[0]:<26}{stats[3]:<18}{stats[4]:<17}{stats[5]}")
    #loop finish here
    db.close()  

def print_usage_rate():
    '''print all the data nicely'''
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM player WHERE usage_rate ORDER BY usage_rate DESC;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                      Points Per Game   Usage rate (%)   Points Created")
    for stats in results:
        print(f"{stats[0]:<26}{stats[3]:<18}{stats[4]:<17}{stats[5]}")
    #loop finish here
    db.close()  

def print_points_created():
    '''print all the data nicely'''
    db = sqlite3.connect(database)
    cursor = db.cursor()
    sql = 'SELECT * FROM player WHERE points_created ORDER BY points_created DESC;'
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                      Points Per Game   Usage rate (%)   Points Created")
    for stats in results:
        print(f"{stats[0]:<26}{stats[3]:<18}{stats[4]:<17}{stats[5]}")
    #loop finish here
    db.close()  





#main code
while True:
    user_input = input("What would you like to do? \n 1. Print all player names \n 2. Print points per game \n 3. Print usage rate \n 4. Print points created \n 5. Exit \n")
    if user_input == "1":
        print_all_players()
    if user_input == "2":
        print_points_per_game()
    if user_input == "3":
        print_usage_rate()
    if user_input == "4":
        print
    if user_input == "5":
        break
    else:
        print("That is not an option\n")
