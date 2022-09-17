# FastAPI Todo App

**Frontend**: React

**Backend**: FastAPI

**Database**: REDIS

## Installation

*if you are on Ubuntu, you will need to install the following packages before going further. Not sure about other linux distros and other platforms*
```
sudo apt install uvicorn redis-server npm
```

Clone this repository:

```
git clone https://github.com/vishwasluhana/fastapi-todo-app
```

Change your directory

```
cd fastapi-todo-app
```

Install requirements using:

```
pip install -r requirements.txt
```

> *Make sure you have nodejs installed to run frontend*

Frontend is forked from [this](https://github.com/scalablescripts/redis-frontend) repository.

```
git clone https://github.com/scalablescripts/redis-frontend
```

Change your directory

```
cd redis-frontend
```

Install the app

```
npm i
```

Start the app

```
npm start
```

Now, go to `https://redis.com`

Login for free and it will auto-create a database for you.

Copy system generated `Public endpoint` and `Default user password` and paste it in `redis_config.json` file.

Go back to the project directory

```
cd ..
```

Run the application

```
uvicorn main:app --reload
```

Open `http://localhost:3000` to view it in the browser.
