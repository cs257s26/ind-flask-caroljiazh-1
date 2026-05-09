import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    This function comes from psycopg2-sample.py given from the intro DB lab
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection 