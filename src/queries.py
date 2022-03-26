from datetime import date
import sqlite3
from time import sleep


# Support function for login()
# Retrieves user details for a given Epost primary key
# Returns None if primary key matches no registered user
def get_db_user(Epost):
    
    # Executing query
    try:
        con = sqlite3.connect("kaffe.db")    
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Bruker WHERE Epost = ?;", (Epost,))
        #cursor.execute("SELECT * FROM Bruker")
        userdata = cursor.fetchone()
        print('Welcome: ' + str(userdata[-1]))
        sleep(1)
        con.close()
        return userdata
    
        
    except:
        print("error occured")
        sleep(0.2)
        return None
        

# Userstory 1 implementation
# Enables insertion of values into Kaffesmaking table
# Check first to see if entered data match registered coffee
# Returns False if process error is encountered
def add_db_entry(Epost, dict):
    
    # Decomposing dictionary
    Smaksnotater = dict.get("notater")
    Poeng = dict.get("poeng")
    Smaksdato = date.today()
    Kaffenavn = dict.get('kaffenavn')
    Brennerinavn = dict.get('brennerinavn')
    
    # Executing query
    try:
        con = sqlite3.connect("kaffe.db")    
        cursor = con.cursor()
        
        # Found lib-command to enable foreign key constraint
        cursor.execute("PRAGMA foreign_keys = 1")
        #! Above query renders following code section obsolete so it should maybe be removed, but we're not doing DB-performance benchmarks here

        
        # Verifying existance of coffee in DB
        cursor.execute(
            """
            SELECT Kaffenavn, Brennerinavn FROM FerdigKaffe
            WHERE Kaffenavn = ? AND Brennerinavn = ?;
            """, 
            (Kaffenavn, Brennerinavn,)
        )
        
        # Raise error if no matching entry is found
        if cursor.fetchone() == None:
            raise sqlite3.DataError
        
        
        # Execute insertion query
        cursor.execute(
            """
            INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
            VALUES (?,?,?,?,?,?)
            """, 
            (Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn)
        )
        
        con.commit()
        con.close()

    except sqlite3.DataError:
        print('Invalid coffee reference. Either coffe or roaster does not exist')
        return False
        
    except:
        print('Either problem connecting to server of inserting value')
        return False

    return True

# Userstory 2 implementation
# Returns data as list if successful, None if error is encountered
def get_caffeine_addicts():
    
    # Executing query
    try:
        con = sqlite3.connect("kaffe.db")    
        cursor = con.cursor()
        # query gets users who've tasted the most different types of coffee, sorted descending
        cursor.execute(
            """
            SELECT 
                Tastingswithnames.Epost, 
                Tastingswithnames.Navn, 
                Tastingswithnames.tastingcount 

            FROM (

                (SELECT 
                    Epost, 
                    COUNT(Epost) AS tastingcount 
                
                FROM 
                
                    (SELECT DISTINCT 
                        Epost, 
                        Kaffenavn, 
                        Brennerinavn 
                    FROM 
                        
                        Kaffesmaking 
                    
                    WHERE 
                        
                        Kaffesmaking.Smaksdato >= date('now', 'start of year'))
                
                GROUP BY 
                    
                    Epost

                ORDER BY 
                    tastingcount DESC)

                AS Tastings 

            NATURAL JOIN Bruker)

            AS Tastingswithnames;
            """)
    
        # returns 50 top results of query 
        batch = cursor.fetchmany(50)

        # closing connection
        con.close()
        
        return batch
        
    except:
        print("Error encountered, returning to main menu")
        return None
        
# Userstory 3 implementation  
# Returns data as list if successful, None if error is encountered
def get_value_coffe():
    
    try:

        con = sqlite3.connect("kaffe.db")    

        cursor = con.cursor()

        cursor.execute(
        """
        SELECT DISTINCT 
            Kaffenavn, 
            Brennerinavn,
            Kilopris,
            AVG(Poeng) AS AvgScore,
            (AVG(Poeng)/Kilopris)*100 AS ScorePerKr

        FROM
            (SELECT
                Kaffenavn,
                Brennerinavn,
                Poeng,
                SmaksID

            FROM
                Kaffesmaking
            )

        NATURAL JOIN FerdigKaffe

        GROUP BY
            Kaffenavn,
            Brennerinavn

        ORDER BY
            AvgScore DESC;
        """
        )

        data = cursor.fetchmany(50)

        con.close()

        

        return data

    except:

        print('Either problem connecting to server or no matching results')

        return None

# Userstory 4 implementation
# Returns data as list if successful, None if error is encountered
def search_db_for_descripton(description):
    
    # preparing description match pattern
    desc = '%' + description.lower() + '%'
    # Executing query
    try:
        con = sqlite3.connect("kaffe.db")    
        cursor = con.cursor()
        cursor.execute(
            """
            SELECT DISTINCT
                Brennerinavn,
                Kaffenavn

            FROM
                (
                SELECT
                    Brennerinavn,
                    Kaffenavn

                FROM
                    FerdigKaffe

                WHERE lower(Beskrivelse) LIKE ?
                
                
                UNION

                
                SELECT
                    Brennerinavn,
                    Kaffenavn

                FROM
                    Kaffesmaking

                WHERE lower(Smaksnotater) LIKE ?
                );                
            """, 
            (desc,desc,))
        
        data = cursor.fetchmany(50)
        con.close()
        
        return data

    except:
        print('Either problem connecting to server or no matching results')
        return None

# Userstory 5 implementation
# Returns data as list if successful, None if error is encountered
def country_process_search(search_process_tuple, search_countries_tuple):
    
    # start of query
    # ends where processes to match are defined
    query_string_processes = """
            SELECT
                Brennerinavn,
                Kaffenavn

            FROM(
                SELECT
                    *
                
                FROM
                    FerdigKaffe
                
                JOIN (

                    SELECT
                        PartiID,
                        Land

                    FROM (
                        SELECT
                            *
                        
                        FROM
                            (SELECT 
                                GaardsID,
                                PartiID 

                            FROM 
                                Kaffeparti 

                            WHERE ForedlingsID = """
    
    # middle of query
    # ends where countries to match are defined
    query_string_countries = """
                        )
                        
                        NATURAL JOIN (
                            SELECT 
                                GaardsID, 
                                Land 

                            FROM 
                                Kaffegaard 

                            NATURAL JOIN Plassering

                            AS GaardsIdMedLand
                        )
                    )

                    WHERE Land = """
    
    # final part of query
    query_string_final = """

                ) AS RCCoffee

                ON 
                    FerdigKaffe.PartiID = RCCoffee.PartiID
            );
        """

    # defining process match pattern
    for i in range(len(search_process_tuple)-1):
        query_string_processes += "'" + search_process_tuple[i][0] + "'" + ' OR ForedlingsID = '
    
    query_string_processes += "'" + search_process_tuple[-1][0] + "'"
    
    # defining country match pattern
    for i in range(len(search_countries_tuple)-1):
        query_string_countries += "'" + search_countries_tuple[i][0] + "'" + ' OR Land = '
    
    query_string_countries += "'" + search_countries_tuple[-1][0] + "'"

    # putting query together
    query_string = query_string_processes + query_string_countries + query_string_final
    
    # Executing query
    try:
        con = sqlite3.connect("kaffe.db")    
        cursor = con.cursor()
        cursor.execute(query_string)
        
        # returns 50 top results of query 
        batch = cursor.fetchmany(50)

        # closing connection
        con.close()
        return batch
        
    except:
        print("Error encountered, returning to main menu")
        return None

# Supportfunctions for country_process_search()

# Returns all processes registered in DB
def get_processes():
# Executing query
    try:
        con = sqlite3.connect("kaffe.db")    
        cursor = con.cursor()
        cursor.execute(
            """
            SELECT Metodenavn
            FROM Foredlingsmetode;
            """
        )
        
        raw_data = cursor.fetchmany(50)
        data = []
        
        [data.append(i[0]) for i in raw_data]
        
        con.close()
        
        return data

    except:
        print('Either problem connecting to server or no matching results')
        return None

# Returns all distinct countries registered in DB
def get_countries():
    # Executing query
    try:
        con = sqlite3.connect("kaffe.db")    
        cursor = con.cursor()
        cursor.execute(
            """
            SELECT DISTINCT Land
            FROM Plassering;
            """
        )
        
        raw_data = cursor.fetchmany(50)
        data = []
        
        [data.append(i[0]) for i in raw_data]
        
        con.close()
        
        return data

    except:
        print('Either problem connecting to server or no matching results')
        return None

