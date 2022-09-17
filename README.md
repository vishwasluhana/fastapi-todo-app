# FastAPI Todo App

Frontend: React
Backend: FastAPI
Database: REDIS

## Installation

*if you're on Ubuntu, you'll need to run these commands on terminal before going further. Not sure about other linux distros and other platforms*
```
sudo apt install uvicorn redis-server npm
```

Clone this repository:

```
git clone https://github.com/vishwasluhana/fastapi-todo-app
```

```
cd fastapi-todo-app
```

Install requirements using:

```
pip install -r requirements.txt
```

*Make sure you have nodejs install to run frontend*
Frontend is forked from [this](https://github.com/scalablescripts/redis-frontend) repository.

```
git clone https://github.com/scalablescripts/redis-frontend
```

```
cd redis-frontend
```

```
npm i
```

```
npm start
```

Go to `https://redis.com`

Login for free and it will auto-create a database for you.

Copy system generated `Public endpoint` and `Default user password` and paste it in `redis_config.json` file.


go back to the project directory
```
cd ..
```
Run the application

```
uvicorn main:app --reload
```

Open `http://localhost:3000` to view it in the browser.