# KaffeDB

## Project description:

A simple database application written in python 3 using sqlite3 for an introductory database course. Allows a user to log in as a user, and then execute SQL queries to input data and search through a database via a simple to use command line interface. Inputs include selecting options from a list or writing simple text input.

## Prequisites

Required technologies with corresponding install commands where relevant:

- Python 3.8+

- sqlite3 for python: `pip install sqlite3`

- pick: `pip install pick`

- tabulate: `pip install tabulate`

The project assumes a file named `kaffe.db` to present within the project directory.

To populate database with mock data, run the `load_into_db.py`

The project should now be ready to go.

## How to use

To use the app you need to log in using a pre-registered valid user. Because the app was written under tight time-constraints it does not include the option to register a new account except for executing raw queries against the database. Passwords are also stored as raw text strings which is obviously a major major limitation, but I refer again to the tight schedule.

One valid user is:
- Email: henrik@gmail.com
- Password: veldigsikkertpassord123

Because of a lack of security specifications and time-constraints, the database includes no password-hashing etc., so the security is minimal/nonexistent.
As this is primarily an exercise in applying SQL and absolutely not a serious production ready database, this is acceptable.
A valid user can be found by looking through the database with a database-viewer tool or reading through the `users` list in `load_into_db.py`
Until valid login credentials have been entered, the application should inform you what error you have commited with your input, and then reprompt you to ented valid credentials.

You should now be faced with a menu. Use the up/down arrows on your keyboard to navigate, then enter to select an option.
This should bring you to a similar menu or prompt you for text input, depending on which sub-menu you enter.
When presented with query results you should be able to look at the table until a keyboard-interrupt is provided.
In the integrated VS Code terminal enter `Ctrl + C` (on windows) to return to main menu
