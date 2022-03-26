import sqlite3


# Format:
# (email, passord, navn)
users = [
    """
    INSERT INTO Bruker(Epost, Passord, Navn)
    VALUES ('henrik@gmail.com', 'veldigsikkertpassord123', 'Henrik Brinch');
    """,
    """
    INSERT INTO Bruker(Epost, Passord, Navn)
    VALUES ('victoria@mail.com', 'ekstremtsikkertpassord123', 'Victoria Kallerud');
    """,
    """
    INSERT INTO Bruker(Epost, Passord, Navn)
    VALUES ('elon@muskrat.space', 'markedsmanipuleringerlættis', 'Elon Musk');
    """,
    """
    INSERT INTO Bruker(Epost, Passord, Navn)
    VALUES ('jeff@lexcorp.villian', 'Myrocketisbiggerthanyours', 'Jeff Luthor Bezoz');
    """,
    """
    INSERT INTO Bruker(Epost, Passord, Navn)
    VALUES ('mark@thezucc.robot', 'lookingforgenuinehumanconnection', '0x6D61726B207A75636B657262657267');
    """,
    """
    INSERT INTO Bruker(Epost, Passord, Navn)
    VALUES ('stoore@vanligefolkstur.no', '0%arveavgiftersweet!', 'Jonas Gahr Støre');
    """
]

# Format:
# (artsnavn)
coffe_species = [
    """
    INSERT INTO Kaffeart (Artsnavn)
    VALUES ('robusta');
    """,
    """
    INSERT INTO Kaffeart (Artsnavn)
    VALUES ('arabica');
    """,
    """
    INSERT INTO Kaffeart (Artsnavn)
    VALUES ('liberica');
    """
]

# Format:
# (navn_vX, prosessbeskrivelse)
processes = [
    """
    INSERT INTO Foredlingsmetode (Metodenavn, Prosessbeskrivelse)
    VALUES ('vasket_v1', 'Dynket i såpebad');
    """,
    """
    INSERT INTO Foredlingsmetode (Metodenavn, Prosessbeskrivelse)
    VALUES ('baertorket_v1', 'lagt i et fuktig rom for å råtne');
    """,
    """
    INSERT INTO Foredlingsmetode (Metodenavn, Prosessbeskrivelse)
    VALUES ('anaerobisk_fermentert_v1', 'kastet ut i verdenrommet der det ikke er luft for å råtne');
    """
]

# Format:
# (region, land)
regions = [
    """
    INSERT INTO Plassering (Region, Land)
    VALUES ('Nyeri', 'Kenya');
    """,
    """
    INSERT INTO Plassering (Region, Land)
    VALUES ('Chinacla', 'Honduras');
    """,
    """
    INSERT INTO Plassering (Region, Land)
    VALUES ('Atnago', 'Ethiopia');
    """,
    """
    INSERT INTO Plassering (Region, Land)
    VALUES ('Khalid Shifa', 'Rwanda');
    """,
    """
    INSERT INTO Plassering (Region, Land)
    VALUES ('Tecapa-Chinameca', 'El Salvador');
    """,
    """
    INSERT INTO Plassering (Region, Land)
    VALUES ('Minas Gerais', 'Brasil');
    """,
    """
    INSERT INTO Plassering (Region, Land)
    VALUES ('Huila', 'Colombia');
    """,
    """
    INSERT INTO Plassering (Region, Land)
    VALUES ('Santa Ana', 'El Salvador');
    """
]

# Format:
# (gaardsID, gaardsnavn, moh, region)
coffee_farms = [
    """
    INSERT INTO Kaffegaard
    VALUES (1,'Los hermanos coffee', 1800, 'Huila'); --@ pass på at noe kaffe er laget her
    """,
    """
    INSERT INTO Kaffegaard
    VALUES (2,'Ikke bygget på brent regnskog', 1300, 'Minas Gerais');
    """,
    """
    INSERT INTO Kaffegaard
    VALUES (3,'We farmin coffee', 2200, 'Khalid Shifa'); --@ pass på at noe kaffe er laget her
    """,
    """
    INSERT INTO Kaffegaard
    VALUES (4,'This is a farm', 2500, 'Atnago');
    """,
    """
    INSERT INTO Kaffegaard
    VALUES (5,'Coffee farm', 2700, 'Chinacla');
    """,
    """
    INSERT INTO Kaffegaard
    VALUES (6,'Generating fake data is boring', 1500, 'Nyeri');
    """,
    """
    INSERT INTO Kaffegaard
    VALUES (7,'Nombre de Dios', 1500, 'Santa Ana');
    """
]

# Format:
# (partiID, innhøstingsår, kilopris, prosessnavn, gaardsID)
#TODO: Implementer AUTOINCREMENT?
coffee_shipments = [
    """
    INSERT INTO Kaffeparti
    VALUES (1,2021, 3.5, 'vasket_v1', 3);
    """,
    """
    INSERT INTO Kaffeparti
    VALUES (2,2022, 4.5, 'baertorket_v1', 1);
    """,
    """
    INSERT INTO Kaffeparti
    VALUES (3,2021, 2.5, 'baertorket_v1', 3);
    """,
    """
    INSERT INTO Kaffeparti
    VALUES (4,2021, 3.5, 'vasket_v1', 4);
    """,
    """
    INSERT INTO Kaffeparti
    VALUES (5,2021, 8, 'baertorket_v1', 7);
    """,
    """
    INSERT INTO Kaffeparti
    VALUES (6,1999, 3.5, 'vasket_v1', 3);
    """,

]

# Format:
# (kaffenavn, brennerinavn, brenningsgrad, brenningsdato, beskrivelse, kilopris, partiID)
finished_coffee = [
    """
    INSERT INTO FerdigKaffe
    VALUES ('Vinterkaffe 2022', 'Jacobsen & Svart', 1, '2022-01-20', 'En velsmakende og kompleks kaffe for mørketiden', 600, 5);
    """,
    """
    INSERT INTO FerdigKaffe
    VALUES ('Mamma Mia', 'ABBA foods', 2, '2008-01-01', 'En nostalgisk floral kaffe med en dansende smaksprofil', 850, 1);
    """,
    """
    INSERT INTO FerdigKaffe
    VALUES ('Gusto', 'French & Press', 3, '2020-09-17', 'Kaffe. På fransk vis', 580, 3);
    """,
    """
    INSERT INTO FerdigKaffe
    VALUES ('Christmas Roast 2021', 'Starbucks', 3, '2021-11-11', 'A seasonal blend to cozy up with', 930, 2);
    """,
    """
    INSERT INTO FerdigKaffe
    VALUES ('Java', 'Coop kaffe', '1', '2022-02-13', 'En klassisk velsmakende kaffe', 395, 4);
    """,
    """
    INSERT INTO FerdigKaffe
    VALUES ('Gammelkaffe', 'Ye Olde brenneri', '1', '1999-02-13', 'En gammel kaffe', 295, 6);
    """

]

# Format:
# (Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn)
coffee_tastings = [
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('notes of citrus, red fruits',1,'2020-06-11','elon@muskrat.space','Mamma Mia', 'ABBA foods');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('spiced with notes of citrus',2,'2021-02-1','jeff@lexcorp.villian','Gusto', 'French & Press');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('honeylike taste with aftertaste of red fruits',3,'2022-03-24','jeff@lexcorp.villian','Java', 'Coop kaffe');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('floral coffee',4,'2022-01-15','elon@muskrat.space','Gusto', 'French & Press');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Red fruits and gingerbread (I do not like gingerbread)',5,'2021-12-24','jeff@lexcorp.villian','Christmas Roast 2021', 'Starbucks');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('starting to go old, still notes of sweet floral intensity',6,'2022-01-25','jeff@lexcorp.villian','Christmas Roast 2021', 'Starbucks');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('hot, summer, red fruits',7,'2021-06-21','stoore@vanligefolkstur.no','Mamma Mia', 'ABBA foods');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Very good, but prefer it as iced coffee',8,'2022-01-03','stoore@vanligefolkstur.no','Gusto', 'French & Press');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Very good, made it as iced coffe by forgetting it outside overnight',9,'2022-01-03','stoore@vanligefolkstur.no','Gusto', 'French & Press');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Sublime, definitely some stone fruits. Check out my coffee-blog at: isimpforjameshoffman.com',10,'2022-02-18','elon@muskrat.space','Gammelkaffe', 'Ye Olde brenneri');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Spring coffe, therefore floral',0,'2022-03-01','mark@thezucc.robot','Java', 'Coop kaffe');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Hot coffee winter',1,'2022-01-07','henrik@gmail.com','Mamma Mia', 'ABBA foods');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Hot coffee summer',2,'2021-07-01','henrik@gmail.com','Mamma Mia', 'ABBA foods');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Tastes a lot like pie',3,'2021-07-22','mark@thezucc.robot','Gammelkaffe', 'Ye Olde brenneri');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Tastes like pie, but only in the US',4,'2022-03-14','mark@thezucc.robot','Gammelkaffe', 'Ye Olde brenneri');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('is it floral maybe?',5,'2022-03-23','victoria@mail.com','Java', 'Coop kaffe');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Floral notes I think',6,'2022-01-05','victoria@mail.com','Vinterkaffe 2022', 'Jacobsen & Svart');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Not enought water',7,'2022-02-17','victoria@mail.com','Vinterkaffe 2022', 'Jacobsen & Svart');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('Smells like a financial crisis',8,'2008-08-28','mark@thezucc.robot','Gammelkaffe', 'Ye Olde brenneri');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('definitely coffee, quite nice',9,'2011-04-29','stoore@vanligefolkstur.no','Gammelkaffe', 'Ye Olde brenneri');
    """,
    
    """
    INSERT INTO Kaffesmaking(Smaksnotater, Poeng, Smaksdato, Epost, Kaffenavn, Brennerinavn) 
    VALUES ('floral coffee of the millenium',10,'2000-01-01','mark@thezucc.robot','Gammelkaffe', 'Ye Olde brenneri');
    """,
    
]

# Format:
relations = [
    """
    INSERT INTO Inneholder
    VALUES (1, 'arabica'); --@
    """,
    """
    INSERT INTO Dyrker
    VALUES (1, 'arabica'); --@
    """
]

# Drops all tables:
db_delete = [
    'DROP TABLE Bruker;',
    'DROP TABLE Kaffesmaking;',
    'DROP TABLE FerdigKaffe;',
    'DROP TABLE Dyrker;',
    'DROP TABLE Foredlingsmetode;',
    'DROP TABLE Inneholder;',
    'DROP TABLE Kaffeart;',
    'DROP TABLE Kaffegaard;',
    'DROP TABLE Kaffeparti;',
    'DROP TABLE Plassering;'
]

# Declares all tables:
db_create = [
    """    
    CREATE TABLE Bruker (
        Epost   TEXT NOT NULL,
        Passord TEXT NOT NULL, --@ideelt sett en passord-hash, men det kan bli vanskelig
        Navn    TEXT NOT NULL,
        CONSTRAINT Bruker_PK PRIMARY KEY (Epost)
    );
    """,
    """
    CREATE TABLE Plassering (
    Region  TEXT    NOT NULL,
    Land    TEXT    NOT NULL,
    CONSTRAINT Plassering_PK PRIMARY KEY (Region)
    );
    """,
    """
    CREATE TABLE Foredlingsmetode (
    Metodenavn          TEXT    NOT NULL,
    Prosessbeskrivelse  TEXT    NOT NULL    UNIQUE, --@ 2 metoder kan ikke ha samme beskrivelse, for da er det samme metode
    CONSTRAINT Foredlingsmetode_PK PRIMARY KEY (Metodenavn)
    );
    """,
    """
    CREATE TABLE Kaffeart (
    Artsnavn TEXT   NOT NULL,
    CONSTRAINT Kaffeart_PK PRIMARY KEY (Artsnavn)
    );
    """,
    """
    CREATE TABLE Kaffegaard (
    GaardsID    INTEGER     NOT NULL,
    Gaardsnavn  TEXT        NOT NULL,
    MOH         INT         NOT NULL,
    Region      TEXT        NOT NULL,
    CONSTRAINT Kaffegaard_PK    PRIMARY KEY (GaardsID),
    CONSTRAINT Kaffegaard_FK    FOREIGN KEY (Region) REFERENCES Plassering(Region)
        ON UPDATE CASCADE
        ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE Kaffeparti (
    PartiID         INTEGER    NOT NULL,
    Innhostingsaar  INT        NOT NULL, --@Constraint: lavere enn årstall nå, håndteres av app
    Kilopris        FLOAT      NOT NULL, --@ database er ikke finansiell, floatingpoint-error er akseptabelt
    ForedlingsID    TEXT       NOT NULL,
    GaardsID        INTEGER        NOT NULL,
    CONSTRAINT Kaffeparti_pk     PRIMARY KEY (PartiID),
    CONSTRAINT Kaffeparti_FK1    FOREIGN KEY (GaardsID) REFERENCES Kaffegaard(GaardsID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Kaffeparti_FK1    FOREIGN KEY (ForedlingsID) REFERENCES Foredlingsmetode(Metodenavn)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Kilopris          CHECK(Kilopris >= 0)
    );
    """,
    """
    CREATE TABLE FerdigKaffe (
        Kaffenavn       TEXT       NOT NULL,
        Brennerinavn    TEXT       NOT NULL,
        Brenningsgrad   INT        NOT NULL, --@ 1 er lys, 3 er mørk. Verdi må være i [1,3]. Display mot bruker defineres av python dictionary
        Dato            DATE       NOT NULL, --@ Må være i fortiden, håndteres av input-validation i app
        Beskrivelse     TEXT       NOT NULL,
        Kilopris        REAL       NOT NULL, --@ database er ikke finansiell, floatingpoint-error er akseptabelt
        PartiID         INTEGER    NOT NULL,
        CONSTRAINT FerdigKaffe_PK   PRIMARY KEY (Kaffenavn, Brennerinavn),
        CONSTRAINT FerdigKaffe_FK   FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
        CONSTRAINT Brenningsgrad    CHECK(Brenningsgrad >= 1 AND Brenningsgrad <= 3),
        CONSTRAINT Kilopris         CHECK(Kilopris >= 0)
    );
    """,
    """
    CREATE TABLE Kaffesmaking (
        SmaksID         INTEGER  PRIMARY KEY AUTOINCREMENT,       --@inkludert for å skille mellom like kaffesmakinger på samme dato
        Smaksnotater    TEXT,                   --@bruker vil kanskje ikke skrive notater, bare rangere
        Poeng           INT     NOT NULL,
        Smaksdato       DATE    NOT NULL,
        Epost           TEXT    NOT NULL,
        Kaffenavn       TEXT    NOT NULL,
        Brennerinavn    TEXT    NOT NULL,
        CONSTRAINT Kaffesmaking_FK1   FOREIGN KEY (Epost) REFERENCES Bruker(Epost) 
            ON UPDATE CASCADE
            ON DELETE CASCADE,
        CONSTRAINT Kaffesmaking_FK2   FOREIGN KEY (Kaffenavn, Brennerinavn) REFERENCES FerdigKaffe(Kaffenavn, Brennerinavn)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
        CONSTRAINT Poeng              CHECK(Poeng >= 0 AND Poeng <= 10)
    );
    """,
    """
    CREATE TABLE Inneholder (
        PartiID     INTEGER     NOT NULL,
        Artsnavn    TEXT    NOT NULL,
        CONSTRAINT Inneholder_PK    PRIMARY KEY (PartiID, Artsnavn),
        CONSTRAINT Inneholder_FK1   FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
        CONSTRAINT Inneholder_FK2   FOREIGN KEY (Artsnavn) REFERENCES Kaffeart(Artsnavn)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE Dyrker (
        GaardsID INTEGER    NOT NULL,
        Artsnavn TEXT   NOT NULL,
        CONSTRAINT Dyrker_PK    PRIMARY KEY (GaardsID, Artsnavn),
        CONSTRAINT Dyrker_FK1   FOREIGN KEY (GaardsID) REFERENCES Kaffegaard(GaardsID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
        CONSTRAINT Dyrker_FK2   FOREIGN KEY (Artsnavn) REFERENCES Kaffeart(Artsnavn)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    );
    """
]

# Opens DB connection
con = sqlite3.connect("kaffe.db")    
cursor = con.cursor()

# Drops all tables
for i in db_delete:
    
    try:
        cursor.execute(i)
        con.commit()

    except:
        None

# Declares all tables
for i in db_create:
    
    try:
        cursor.execute(i)
        con.commit()
    except:
        print("This failed:")
        print(i)

# Fills DB with mock users
[cursor.execute(i) for i in users]
con.commit()    

# Fills DB with mock coffee species
[cursor.execute(i) for i in coffe_species]
con.commit()    

# Fills DB with mock processes
[cursor.execute(i) for i in processes]
con.commit()    

# Fills DB with mock regions
[cursor.execute(i) for i in regions]
con.commit()    

# Fills DB with mock coffee farms
[cursor.execute(i) for i in coffee_farms]
con.commit()    

# Fills DB with mock coffee shipments
[cursor.execute(i) for i in coffee_shipments]
con.commit()    

# Fills DB with mock finished coffee
[cursor.execute(i) for i in finished_coffee]
con.commit()    

# Fills DB with mock coffee tastings
[cursor.execute(i) for i in coffee_tastings]
con.commit()    

# Fills DB with mock relations
[cursor.execute(i) for i in relations]
con.commit()    

# Closes DB connection
con.close()

