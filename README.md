# Movie Recommendation AI

## Project setup

In order to run app locally, you must initialize the front-end and back-end in two different terminals.
Once you have the project initialized, you should be able to open the application locally at:

http://localhost:8081/

## Front-end (Client)
To initialize the front-end(Vue application), in your terminal follow this commands:
```
cd client
yarn
yarn serve
```

## Back-end (Server)
To initialize the back-end server, you must add a file called '.env' in the server folder and add you API from TMDb,
there is a file called .env-example for reference

then run the following commands in a separate terminal to initialize the server:

```
cd server
pip freeze > requirements.txt
source venv/bin/activate
python run.py
```
