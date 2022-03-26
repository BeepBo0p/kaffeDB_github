## Prequisites

- Python 3.8+

- sqlite3: `pip install sqlite3`

- pick: `pip install pick`

- tabulate: `pip install tabulate`

To populate database with mockdata, run `load_into_db.py`

The project should now be ready to go

## How to use

To operate DB you need to log in using a pre-registered valid user.
Because of time-constraints the database includes no password-hashing etc., so the security is minimal/nonexistent.
We found this acceptable as there were no security constraints specified in the user-stories other than an implicit association between entered data and a user.
A valid user can be found by looking through the database with a database-viewer tool or reading through the `users` list in `load_into_db.py`
Until valid login credentials have been entered, the application should inform you what error you have commited with your input, and then reprompt you to ented valid credentials.
You should now be faced with a menu. Use the up/down arrows on your keyboard to navigate, then enter to select an option.
This should bring you to a similar menu or prompt you for text input, depending on which sub-menu you enter.
When presented with query results you should be able to look at the table until a keyboard-interrupt is provided.
In the integrated VS Code terminal enter `Ctrl + C` (on windows) to return to main menu

## See L2 project documentation pdf for proper documentation