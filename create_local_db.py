import psycopg2
from psycopg2 import sql

from dotenv import load_dotenv
import os

from django.contrib.auth.models import User

load_dotenv()


# This password will vary depending on your local PostgreSQL log-in
PSQL_PASSWORD = os.getenv('PSQL_PASSWORD')

DB_ADMIN = os.getenv('DB_ADMIN')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DJANGO_ADMIN = os.getenv('DJANGO_ADMIN')
DJANGO_PASSWORD = os.getenv('DJANGO_PASSWORD')

# establishing the connection

connection = psycopg2.connect(user='postgres',
                              password=PSQL_PASSWORD,
                              host="127.0.0.1",
                              port="5432")

connection.autocommit = True

cursor = connection.cursor()

cursor.execute(sql.SQL('DROP DATABASE IF EXISTS muse;'))
cursor.execute(sql.SQL(f'DROP USER IF EXISTS {DB_ADMIN};'))
cursor.execute(sql.SQL('CREATE DATABASE muse;'))
cursor.execute(
    sql.SQL(f"CREATE USER {DB_ADMIN} WITH PASSWORD '{DB_PASSWORD}';"))
cursor.execute(
    sql.SQL(f"GRANT ALL PRIVILEGES ON DATABASE muse TO {DB_ADMIN};"))

print("Successfully created muse database")


os.system('python3 manage.py createsuperuser')

# Programatically create a superuser for Django's admin page, without an email address
# super_user = User.objects.create_superuser(
#    username=DJANGO_ADMIN, password=DJANGO_PASSWORD)

# super_user.save()

if (connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection closed")
