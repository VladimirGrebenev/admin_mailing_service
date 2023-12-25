# About admin_mailing_service
admin service for mailing messages to clients phones.

# Stack
- Python 3.10
- Django 4.2.8
- Djangoresframework 3.14
- Redis
- Celery
- Node.js
- React
- more info in requirements.py 


# to start app in docker
1. pull project
2. switch to deploy branch: git checkout deploy
3. create you .env file from sample [.env_sample](https://github.com/VladimirGrebenev/admin_mailing_service/blob/deploy/admin_mailing/.env_sample)
4. go to frontend dir and build: npm run build
5. install [docker and docker-compose](https://www.docker.com/)
6. go to the dir /admin_mailing_service/
7. run docker-compose: docker-compose up --build
8. go to the swagger [http://0.0.0.0:8000/docs/](http://0.0.0.0:8000/docs/)
9. if you wanted not only see, but create some dispatches, you must create user /user/register/
10. and login with new user [http://0.0.0.0:8000/api-auth/login](http://0.0.0.0:8000/api-auth/login)
11. frontend on docker coming soon...

# To start working development

1. pull master from github
2. in terminal go to working dir: cd admin_mailing_service/admin_mailing/
3. don't foget install posgtres, redis, celery
4. create postgres database
5. edit your .env file to set you settings, you can check .env_sample file
6. don't forget set you CORS_ALLOWED_ORIGINS in settings, don't use * set_all, set only your needed CORS
7. in terminal install all requirements: pip install -r requirements.txt
8. in terminal start redis: redis-server
9. in terminal start celery: celery -A admin_mailing worker --loglevel=info
10. in terminal staert celery beat: celery -A admin_mailing beat
11. in terminal start servise: python manage.py runserver
12. go to the http://127.0.0.1:8000/ or http://127.0.0.1:8000/swagger/
13. to use all opportunities you must registred here (http://127.0.0.1:8000/register/) id=null ,
    and after that login here (http://127.0.0.1:8000/api-auth/login/).
14. if you what use front end WEB UI, you must install node js ( sudo apt install nodejs),
15. and install all js-requirements from frontend dir: cd frontend,  npm install.
16. for react you need install some libraries:
     - npm install bulma ;
     - npm install react-router-dom ;
17. so, maybe you what to know what frontend I make by React - sudo npx create-react-app frontend
18. ок, to use frontend WEB UI, you must go to frontend dir (cd frontend), and use command (npm run start), use WEB UI on localhost:3000
19. enjoy

# Logging
- all logging you can find in app dir in the app.log file
- logger setting in the admin_mailing_service/admin_mailing/logging_config.py

# API docs
you are welcome to use Swagger UI, just add link /doc/ in your browser (http://127.0.0.1:8000/doc/)

# Testing 
- to run tests please go to the working dir: cd admin_mailing_service/admin_mailing/
- and run in terminal tis command: python manage.py test main_app.tests users.tests
- !!! Dispatch tests only work when celery + redis is running, you can uncomment them

# TODO:
- docker package
- registration by OAuth2 
