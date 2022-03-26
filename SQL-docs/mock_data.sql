
--@Entities with no foreign key dependency

--@ insert user info
--@Block
INSERT INTO Bruker(Epost, Passord, Navn)
VALUES ('henrik@gmail.com', 'veldigsikkertpassord123', 'Henrik Brinch');

INSERT INTO Bruker(Epost, Passord, Navn)
VALUES ('victoria@mail.com', 'ekstremtsikkertpassord123', 'Victoria Kallerud');

INSERT INTO Bruker(Epost, Passord, Navn)
VALUES ('elon@muskrat.space', 'markedsmanipuleringerlættis', 'Elon Musk');

INSERT INTO Bruker(Epost, Passord, Navn)
VALUES ('jeff@lexcorp.villian', 'Myrocketisbiggerthanyours', 'Jeff Luthor Bezoz');

INSERT INTO Bruker(Epost, Passord, Navn)
VALUES ('mark@thezucc.robot', 'lookingforgenuinehumanconnection', '0x6D61726B207A75636B657262657267');

INSERT INTO Bruker(Epost, Passord, Navn)
VALUES ('stoore@vanligefolkstur.no', '0%arveavgiftersweet!', 'Jonas Gahr Støre');




--@ insert coffee species
--@Block
INSERT INTO Kaffeart (Artsnavn)
VALUES ('robusta');

INSERT INTO Kaffeart (Artsnavn)
VALUES ('arabica');

INSERT INTO Kaffeart (Artsnavn)
VALUES ('liberica');




--@ insert foredlingsmetoder
--@Block
INSERT INTO Foredlingsmetode (Metodenavn, Prosessbeskrivelse)
VALUES ('vasket_v1', 'Dynket i såpebad');

INSERT INTO Foredlingsmetode (Metodenavn, Prosessbeskrivelse)
VALUES ('baertorket_v1', 'lagt i et fuktig rom for å råtne');

INSERT INTO Foredlingsmetode (Metodenavn, Prosessbeskrivelse)
VALUES ('anaerobisk_fermentert_v1', 'kastet ut i verdenrommet der det ikke er luft for å råtne');





--@ insert region & land
--@Block
INSERT INTO Plassering (Region, Land)
VALUES ('Nyeri', 'Kenya');

INSERT INTO Plassering (Region, Land)
VALUES ('Chinacla', 'Honduras');

INSERT INTO Plassering (Region, Land)
VALUES ('Atnago', 'Ethiopia');

INSERT INTO Plassering (Region, Land)
VALUES ('Khalid Shifa', 'Rwanda');

INSERT INTO Plassering (Region, Land)
VALUES ('Tecapa-Chinameca', 'El Salvador');

INSERT INTO Plassering (Region, Land)
VALUES ('Minas Gerais', 'Brasil');

INSERT INTO Plassering (Region, Land)
VALUES ('Huila', 'Colombia');

INSERT INTO Plassering (Region, Land)
VALUES ('Santa Ana', 'El Salvador');






--@Entities with foreign key dependency

--@ insert kaffegaard
--@block
INSERT INTO Kaffegaard
VALUES ('Los hermanos coffee', 1800, 'Huila'); --@ pass på at noe kaffe er laget her

INSERT INTO Kaffegaard
VALUES ('Ikke bygget på brent regnskog', 1300, 'Minas Gerais');

INSERT INTO Kaffegaard
VALUES ('We farmin coffee', 2200, 'Khalid Shifa'); --@ pass på at noe kaffe er laget her

INSERT INTO Kaffegaard
VALUES ('This is a farm', 2500, 'Atnago');

INSERT INTO Kaffegaard
VALUES ('Coffee farm', 2700, 'Chinacla');

INSERT INTO Kaffegaard
VALUES ('Generating fake data is boring', 1500, 'Nyeri');

INSERT INTO Kaffegaard
VALUES ('Nombre de Dios', 1500, 'Santa Ana');



--@ insert kaffeparti
--@block
INSERT INTO Kaffeparti
VALUES (2021, 3.5, 'vasket_v1', 'We farmin coffee');

INSERT INTO Kaffeparti
VALUES (2022, 4.5, 'baertorket_v1', 'Los hermanos coffee');

INSERT INTO Kaffeparti
VALUES (2021, 2.5, 'baertorket_v1', 'We farmin coffee');

INSERT INTO Kaffeparti
VALUES (2021, 3.5, 'vasket_v1', 'This is a farm');

INSERT INTO Kaffeparti
VALUES (2021, 8, 'baertorket_v1', 'Nombre de Dios');





--@insert FerdigKaffe
--@block
INSERT INTO FerdigKaffe
VALUES ('Vinterkaffe 2022', 'Jacobsen & Svart', 1, '20/1/2022');

INSERT INTO FerdigKaffe
VALUES ('Mamma Mia', 'ABBA foods', 2, '1/1/2008', 'En nostalgisk kaffe med en dansende smaksprofil', 850);

INSERT INTO FerdigKaffe
VALUES ('Gusto', 'French & Press', 3, '17/9/2020', 'Kaffe. På fransk vis', 580);

INSERT INTO FerdigKaffe
VALUES ('Christmas Roast 2021', 'Starbucks', 3, '11/11/2021', 'A seasonal blend to cozy up with', 930);

INSERT INTO FerdigKaffe
VALUES ('Java', 'Coop kaffe', '1', '13/2/2022', 'En klassisk velsmakende kaffe', 395);





--@Relations
INSERT INTO Inneholder
VALUES (1, 'arabica'); --@



INSERT INTO Dyrker
VALUES (1, 'arabica'); --@



