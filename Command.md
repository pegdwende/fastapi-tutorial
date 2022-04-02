Run Server: uvicorn main:app --releod main is the entry point file and app is the variable assigned to the Fast Api Object 

    https://fastapi.tiangolo.com/tutorial/first-steps/

PostGressRoot Db: db1234    

activate virtual environment: c:/Learning/fastApi/venv-fast-api/Scripts/activate.bat

pip freeze > requirements.txt : dump packages into requirement.txt file
pip install -r requirements.txt : install all packages in the requirement.txt file 

#Alemenbic
alember upgrade heads : migrate latest revision
alembic revision --autogenerate  -m "add phone number" : autogererate migration files based on models changes
alembic current :gives the current version of the migration hash
alembic revision : create revision
alembic history  : history of revisions 
