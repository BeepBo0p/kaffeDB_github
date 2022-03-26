
--@Block
--@ DATABASE DELETE TOOL
DROP TABLE Bruker;
DROP TABLE Kaffesmaking;
DROP TABLE FerdigKaffe;
DROP TABLE Dyrker;
DROP TABLE Foredlingsmetode;
DROP TABLE Inneholder;
DROP TABLE Kaffeart;
DROP TABLE Kaffegaard;
DROP TABLE Kaffeparti;
DROP TABLE Plassering;

--@Block
CREATE TABLE Bruker (
    Epost   TEXT NOT NULL,
    Passord TEXT NOT NULL, --@ideelt sett en passord-hash, men det kan bli vanskelig
    Navn    TEXT NOT NULL,
    CONSTRAINT Bruker_PK PRIMARY KEY (Epost)
);


--@Block
CREATE TABLE Plassering (
   Region  TEXT    NOT NULL,
   Land    TEXT    NOT NULL,
   CONSTRAINT Plassering_PK PRIMARY KEY (Region)
);


--@Block
CREATE TABLE Foredlingsmetode (
   Metodenavn          TEXT    NOT NULL,
   Prosessbeskrivelse  TEXT    NOT NULL    UNIQUE, --@ 2 metoder kan ikke ha samme beskrivelse, for da er det samme metode
   CONSTRAINT Foredlingsmetode_PK PRIMARY KEY (Metodenavn)
);

--@Block
CREATE TABLE Kaffeart (
   Artsnavn TEXT   NOT NULL,
   CONSTRAINT Kaffeart_PK PRIMARY KEY (Artsnavn)
);



--@Block
CREATE TABLE Kaffegaard (
   GaardsID    INT     NOT NULL     AUTOINCREMENT,
   Gaardsnavn  TEXT    NOT NULL,
   MOH         INT     NOT NULL,
   Region      TEXT    NOT NULL,
   CONSTRAINT Kaffegaard_PK    PRIMARY KEY (GaardsID),
   CONSTRAINT Kaffegaard_FK    FOREIGN KEY (Region) REFERENCES Plassering(Region)
       ON UPDATE CASCADE
       ON DELETE CASCADE
);


--@Block
CREATE TABLE Kaffeparti (
   PartiID         INT    NOT NULL     AUTOINCREMENT,
   Innhostingsaar  INT     NOT NULL, --@Constraint: lavere enn årstall nå, håndteres av app
   Kilopris        FLOAT   NOT NULL, --@ database er ikke finansiell, floatingpoint-error er akseptabelt
   ForedlingsID    TEXT    NOT NULL,
   GaardsID        INT    NOT NULL,
   CONSTRAINT Kaffeparti_pk     PRIMARY KEY (PartiID),
   CONSTRAINT Kaffeparti_FK1    FOREIGN KEY (GaardsID) REFERENCES Kaffegaard(GaardsID)
       ON UPDATE CASCADE
       ON DELETE CASCADE,
   CONSTRAINT Kaffeparti_FK1    FOREIGN KEY (ForedlingsID) REFERENCES Foredlingsmetode(Metodenavn)
       ON UPDATE CASCADE
       ON DELETE CASCADE,
   CONSTRAINT Kilopris          CHECK(Kilopris >= 0)
);


--@Block
CREATE TABLE FerdigKaffe (
    Kaffenavn       TEXT    NOT NULL,
    Brennerinavn    TEXT    NOT NULL,
    Brenningsgrad   INT     NOT NULL, --@ 1 er lys, 3 er mørk. Verdi må være i [1,3]. Display mot bruker defineres av python dictionary
    Dato            DATE    NOT NULL, --@ Må være i fortiden, håndteres av input-validation i app
    Beskrivelse     TEXT    NOT NULL,
    Kilopris        REAL    NOT NULL, --@ database er ikke finansiell, floatingpoint-error er akseptabelt
    PartiID         INT    NOT NULL,
    CONSTRAINT FerdigKaffe_PK   PRIMARY KEY (Kaffenavn, Brennerinavn),
    CONSTRAINT FerdigKaffe_FK   FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Brenningsgrad    CHECK(Brenningsgrad >= 1 AND Brenningsgrad <= 3),
    CONSTRAINT Kilopris         CHECK(Kilopris >= 0)
);

--@Block
CREATE TABLE Kaffesmaking (
    SmaksID         INT     NOT NULL    AUTOINCREMENT,       --@inkludert for å skille mellom like kaffesmakinger på samme dato
    Smaksnotater    TEXT,                   --@bruker vil kanskje ikke skrive notater, bare rangere
    Poeng           INT     NOT NULL,
    Smaksdato       DATE    NOT NULL,
    Epost           TEXT    NOT NULL,
    Kaffenavn       TEXT    NOT NULL,
    Brennerinavn    TEXT    NOT NULL,
    CONSTRAINT Kaffesmaking_PK    PRIMARY KEY (SmaksID),
    CONSTRAINT Kaffesmaking_FK1   FOREIGN KEY (Epost) REFERENCES Bruker(Epost) 
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Kaffesmaking_FK2   FOREIGN KEY (Kaffenavn, Brennerinavn) REFERENCES FerdigKaffe(Kaffenavn, Brennerinavn)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Poeng              CHECK(Poeng >= 0 AND Poeng <= 10)
);



--@Block
CREATE TABLE Inneholder (
    PartiID     INT     NOT NULL,
    Artsnavn    TEXT    NOT NULL,
    CONSTRAINT Inneholder_PK    PRIMARY KEY (PartiID, Artsnavn),
    CONSTRAINT Inneholder_FK1   FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Inneholder_FK2   FOREIGN KEY (Artsnavn) REFERENCES Kaffeart(Artsnavn)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);




--@Block
CREATE TABLE Dyrker (
    GaardsID INT    NOT NULL,
    Artsnavn TEXT   NOT NULL,
    CONSTRAINT Dyrker_PK    PRIMARY KEY (GaardsID, Artsnavn),
    CONSTRAINT Dyrker_FK1   FOREIGN KEY (GaardsID) REFERENCES Kaffegaard(GaardsID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT Dyrker_FK2   FOREIGN KEY (Artsnavn) REFERENCES Kaffeart(Artsnavn)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);



