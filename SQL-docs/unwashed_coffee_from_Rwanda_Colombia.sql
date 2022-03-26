
--@select all unwashed coffee-shipments
--@block
SELECT 
    GaardsID,
    PartiID 

FROM 
    Kaffeparti 

WHERE ForedlingsID NOT LIKE '%vasket%';

--@select farms and combine with country
--@block
SELECT 
    GaardsID, 
    Land

FROM 
    Kaffegaard 

NATURAL JOIN Plassering

AS GaardsIdMedLand;

--@Combine each shipment with country, then select shipments from Rwanda and Colombia
--@block
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

        WHERE ForedlingsID NOT LIKE '%vasket%')
    
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

WHERE Land = 'Rwanda' OR 'Colombia';


--@Select coffee and roaster joined on shipments from Colombia and Rwanda
--@block
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

                WHERE ForedlingsID NOT LIKE '%vasket%')
            
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

        WHERE Land = 'Rwanda' OR 'Colombia'

    ) AS RCCoffee

    ON 
        FerdigKaffe.PartiID = RCCoffee.PartiID
);