# Django-assignment

postgres set up:

sudo su - postgres

psql

CREATE DATABASE assignment;

CREATE USER abhijit WITH PASSWORD 'password';

ALTER ROLE abhijit SET client_encoding TO 'utf8';

ALTER ROLE abhijit SET default_transaction_isolation TO 'read committed';

ALTER ROLE abhijit SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE assignment TO abhijit;





Django :

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver





Postman Collection APIs:

Postman Documentation link: https://documenter.getpostman.com/view/7497641/SzRuZXzJ?version=latest#a16d337d-92a7-405b-a844-f614b4997ef4

Postman link : https://www.getpostman.com/collections/1d5d3a23b3236b24d1fd



steps:
1) signup to get jwt token 
2) use this token as Authorization: Bearer token "token"
3) Post, Get, Update and Delete Document
