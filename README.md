# About admin_mailing_service
admin service for mailing messenges to clients phone.

# To start service

1. pull from github
2. in terminal go to working dir: cd admin_mailing_service/admin_mailing/
3. don't foget install posgtres, redis, celery
4. create postgres database
5. edit your .env file to set you settings, you can check .env_sample file
6. in terminal install all requirements: pip install -r requirements.txt
7. in terminal start redis: redis-cerver
8. in terminal start celery: celery -A admin_mailing worker --loglevel=info
9. in terminal staert celery beat: celery -A admin_mailing beat
10. in terminal start servise: python manage.py runserver
11. go to the http://127.0.0.1:8000/ or http://127.0.0.1:8000/swagger/
12. to use all opportunities you must registred here (http://127.0.0.1:8000/register/) id=null ,
    and after that login here (http://127.0.0.1:8000/api-auth/login/).

# Logging
all logging you can find in app dirictory in app.log file

# API docs
you are welcome to use Swagger UI, just add link /doc/ in your browser

# Testing 
- to run tests please go to the working dir: cd admin_mailing_service/admin_mailing/
- and run in terminal tis command: python manage.py test main_app.tests users.tests
