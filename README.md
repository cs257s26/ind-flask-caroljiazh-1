# README

Individual Flask project. This Flask app provides routes to explore global literacy rate and education.

## How to Run

From the top level of the repository, run:

```bash
python3 app.py
```

## Database Setup

`cd` into `ind-flask-caroljiazh-1`, then run `psql`. Execute the following command to copy data into the table:

```sql
\copy schooling FROM 'Data/cleaned_data.csv' DELIMITER ',' CSV;
```

## Routes

Route format:

```
http://127.0.0.1:PORT/literacy-growth/<country>
```

### 1. Literacy Growth by Country

Note: use hyphens instead of spaces for country names.

```
http://127.0.0.1:5000/literacy-growth/France
http://127.0.0.1:5000/literacy-growth/United-States
```

### 2. Average Years of Schooling by Country and Year Range

Also use hyphens if needed:

```
http://127.0.0.1:5000/schooling/France/2000/2020
http://127.0.0.1:5000/schooling/United-States/2010/2020
```

## Command to Run the Tests

```bash
python3 -m unittest Tests/test_routes.py
```

To test the database, run:

```bash
python3 datasource.py
```

## Individual Database Writeup

### 1. Describe the process by which you decided how to represent your data in your database. Include why you selected the number of tables you did, how you decided what data to include and exclude, why you selected the datatypes you did, and what the primary keys are.

I selected country, year, and avg_years_schooling for my cleaned_data.csv. They are named Entity, Code, and Education for 15-64 years hold. Because I did user story 2, which is: "As a student interested in global education trends, I want to look up the average years of schooling in my country for any 5 years in the dataset, and compare it with other countries, so that I can understand how well my country's education system is performing globally during that time period."
These three columns are the only ones that matter. Others like code, literacy rate, population, and region, are irrelevant. I chose VARCHAR for country names since they are text made out of letters, INTEGER for year since years are whole numbers, and FLOAT for avg_years_schooling since there are decimals. The primary key is the combination of country and year, since each country has one value per year.

### 2. Explain how each of your queries represents a user story. What does the query do, and how does this match all or part of a user story?

My first query country_avg_schooling returns the average years of schooling for a country within a given year range. It matches the first part of the user story in which we can give the education rate for a desired time range. It matches the first part of the user story "I want to look up the average years of schooling in my country for any 5 years in the dataset."
My second query top_country_year returns a given number of top countries with the highest average years of schooling within a given year. It matches my latter user story of "compare it with other countries...during that time period." By seeing which countries rank highest in a given year, a student can compare their own country with the top-ranking countries.