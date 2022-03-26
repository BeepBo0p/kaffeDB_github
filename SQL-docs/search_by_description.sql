
--@Choose all matching in Ferdig Kaffe
--@block
SELECT
    Brennerinavn,
    Kaffenavn

FROM
    FerdigKaffe

WHERE lower(Beskrivelse) LIKE ?;

--@Choose all matching in kaffesmakinger
--@block
SELECT
    Brennerinavn,
    Kaffenavn

FROM
    Kaffesmaking

WHERE lower(Beskrivelse) LIKE ?;

--@Select all distinct matching from combined queries
--@block
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
