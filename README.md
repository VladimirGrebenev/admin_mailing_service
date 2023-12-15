# About admin_mailing_service
admin service for mailing messenges to clients phone.

# To start service

1. pull from github
2. in terminal go to working dir: cd admin_mailing_service/admin_mailing/
3. edit your .env file to set you settings, you can check .env_sample file
4. in terminal instal requirements: pip install -r requirements.txt
5. in terminal start redis: redis-cerver
6. in terminal start celery: celery -A admin_mailing worker --loglevel=info
7. in terminal staert celery beat: celery -A admin_mailing beat
8. in terminal start servise: python manage.py runserver

# Logging
all logging you can find in app dirictory in app.log file

# API docs
you are welcome to use Swagger UI, just add link /doc/ in your browser
