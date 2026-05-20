DROP TABLE IF EXISTS education;

CREATE TABLE education (
    country             VARCHAR(100),
    year                INTEGER,
    avg_years_schooling FLOAT,
    literacy_rate       FLOAT,
    women_pct           FLOAT
);