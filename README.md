# admin_mailing_service
admin_mailing_service

# to start service

1. pull from github
2. in terminal go to working dir: cd admin_mailing_service/admin_mailing/
3. in terminal instal requirements: pip install -r requirements.txt
4. in terminal start redis: redis-cerver
5. in terminal start celery: celery -A admin_mailing worker --loglevel=info
6. in terminal start servise: python manage.py runserver
