# Flask Restful Boilerplate

This small repo demonstrates a proper file structure for a Flask Restful app. The folders named *library* and *src* are required.

**database** connection is handled correctly in `library/db/mysql_db.py` and cred for db connection is managed in  `configuration/db.json`.


### How to Run this code:

Create Virtual environment.

`python -m venv env` # For windows, you can google how to create virtual env.


Gunicorn server is used in this code and started from run.sh file, to start run.sh first give execution permission.

`chmod +x run.sh`

After installing all dependencies, run the app by executing command on terminal:

`$ ./run.sh`
