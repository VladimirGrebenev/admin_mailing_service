# About admin_mailing_service
admin service for mailing messenges to clients phones.

# To start working development

1. pull from github
2. in terminal go to working dir: cd admin_mailing_service/admin_mailing/
3. don't foget install posgtres, redis, celery
4. create postgres database
5. edit your .env file to set you settings, you can check .env_sample file
6. don't forget set you CORS_ALLOWED_ORIGINS in settings, don't use * set_all, set only your needed CORS
7. in terminal install all requirements: pip install -r requirements.txt
8. in terminal start redis: redis-cerver
9. in terminal start celery: celery -A admin_mailing worker --loglevel=info
10. in terminal staert celery beat: celery -A admin_mailing beat
11. in terminal start servise: python manage.py runserver
12. go to the http://127.0.0.1:8000/ or http://127.0.0.1:8000/swagger/
13. to use all opportunities you must registred here (http://127.0.0.1:8000/register/) id=null ,
    and after that login here (http://127.0.0.1:8000/api-auth/login/).
14. enjoy

# Logging
- all logging you can find in app dir in the app.log file
- logger setting in the admin_mailing_service/admin_mailing/logging_config.py

# API docs
you are welcome to use Swagger UI, just add link /doc/ in your browser (http://127.0.0.1:8000/doc/)

# Testing 
- to run tests please go to the working dir: cd admin_mailing_service/admin_mailing/
- and run in terminal tis command: python manage.py test main_app.tests users.tests
- !!! Dispatch tests only work when celery + redis is running, you can uncomment them
