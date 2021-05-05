python manage.py dumpdata > backup.json
pip install psycopg2
python manage.py migrate --run-syncdb
python manage.py loaddata backup.json