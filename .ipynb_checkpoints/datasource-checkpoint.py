import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    
    This function's code and comments come from psycopg2-sample.py given in the intro DB lab on Moodle
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection 

def country_avg_schooling(connection, country, start_year, end_year):
    """
    Returns the average years of schooling for a country within a given year range.
    
    Args:
        connection (psycopg2.connection) - the connection to the database
        country (str) - the desired country
        start_year (int) - beginning inclusive year range
        end_year (int) - ending inclusive year range
    Returns:
        list - rows of (country, year, avg_years_schooling) or None if no data
    """
    try:
        cursor = connection.cursor()
        query = """SELECT country, year, avg_years_schooling FROM schooling WHERE LOWER(country) = LOWER(%s) AND year >= %s AND year <= %s ORDER BY year ASC;"""
        cursor.execute(query, (country, start_year, end_year))
        return cursor.fetchall()
        
    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def top_country_year(connection, year, country_number):
    """
    Returns a given number of top countries with the highest average years of schooling within a given year. 
    
    Args:
        connection (psycopg2.connection) - the connection to the database
        year (int) - the designated year
        country_number (int) - the desired number of countries outputted
        
    Return:
        list - a list of the top (input number) countries with the highest average years of schooling in a given year
    """
    try:
        cursor = connection.cursor()
        query = """SELECT country, year, avg_years_schooling FROM schooling WHERE year = %s ORDER BY avg_years_schooling DESC LIMIT %s;"""
        cursor.execute(query, (year, country_number))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def main():
    connection = connect()
    print(country_avg_schooling(connection, 'France', 2015, 2020))
    print(top_country_year(connection, 2020, 5))
    connection.close()

if __name__ == '__main__':
    main()
