

--@select relevant data
--@block
SELECT
    Kaffenavn,
    Brennerinavn,
    Poeng,
    SmaksID
    
FROM
    Kaffesmaking;

--@find average score
--@block
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
    ScorePerKr DESC;
