
--@ select distinct coffetastings
--@block
SELECT DISTINCT 
    Epost, 
    Kaffenavn, 
    Brennerinavn 

FROM 
    Kaffesmaking 

WHERE Kaffesmaking.Smaksdato >= date('now', 'start of year');

--@ select count
--@block
SELECT 

    Epost, 
    
    COUNT(Epost) AS tastingcount 

FROM 
    (SELECT DISTINCT 
        Epost, 
        Kaffenavn, 
        Brennerinavn 
    
    FROM 
        
        Kaffesmaking 
    
    WHERE Kaffesmaking.Smaksdato >= date('now', 'start of year'))

GROUP BY Epost 
ORDER BY tastingcount DESC; 

--@ connect to name
--@block
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