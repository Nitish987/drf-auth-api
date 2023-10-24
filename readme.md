# Softauth server

django rest framework authentication api services

# Steps to setup

### Steps to setup localhost server ***http://127.0.0.1:8000***. This will be done only once.

- Download and install [python](https://www.python.org/downloads/)

> Note: While installing check add to path checkbox.

- Clone this repository

`git clone https://github.com/Nitish987/drf-auth-api-service.git`

- Open the clone repository

> Open the clone repository in vscode and open terminal in it.

- Install virtual environment

`pip install virtualenv`

- Create virtual environment

`virtualenv venv`

> This will create venv folder in current directory.

- Activate virtual environment

`./venv/Scripts/activate`

> If virtual environment is active, it will be showing (venv) in starting on your terminal.

- Install python modules

`pip install -r requirements.txt`

- Change directory

`cd softauth`

- Check if you are in right directory

`ls`

> If manage.py is listed then its correct else move back using [cd ../] command or forward using [cd directory_name]

- Make migrations

`python manage.py makemigrations`

- Migrate

`python manage.py migrate`

> This will create db.sqlite3 database file

- Create super user

`python manage.py createsuperuser`

> Enter admin name, admin email and admin password

# Steps to Start the server

### Steps to start the server whenever you start system.

- Open the clone repository

> Open the clone repository in vscode and open terminal in it.

- Activate virtual environment. Skip this step if virtual environment is already active.

`./venv/Scripts/activate`

> If virtual environment is active, it will be showing (venv) in starting on your terminal.

- Change directory. Skip this step if you are in softauth directory.

`cd softauth`

- Check if you are in right directory

`ls`

> If manage.py is listed then its correct else move back using [cd ../] command or forward using [cd directory_name]

- Start the server

`python manage.py runserver`

> Your server api is live at [http://127.0.0.1:8000](http://127.0.0.1:8000)

> Your admin site is live at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). login to access admin panel with admin email and admin password.