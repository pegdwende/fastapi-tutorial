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


#heroku
git push heroku main : push changes to erroku
heroku logs -t : check heroku logs
heroku run "alembic upgrade heads" : run migration
heroku config:set PGSSLMODE=require : enable ssl for postgres 

#ubuntu server
ssh username@ip : connect to ubuntu virtual machine
sudo apt update && sudo apt upgrade -y : upgrate and update ubuntu
sudo apt install python3-pip : intalling pip
sudo pip3 install virtualenv : installing virtual env
sudo apt install postgresql postgresql-contrib : install postgres
sudo cat /etc/passwd : list of install password 
cd /etc/postgresql/12/main 
sudo vi postgresql.conf : edit postgresql.conf and add listen_addresses ='*' (narrow ips that can access this) to be able to connect from other IP's
sudo vi  pg_hba.conf : change connection method to md5, change Addess allowed for local connection for IPV4 to 0.0.0.0/0 and IPV6 to ::/0 
systemctl restart postgresql : restart application
su - postgres : log into postgress
pg_lsclusters : check cluster status
sudo pg_ctlcluster 12 main start : start postgress cluster
cat /var/log/postgresql/postgresql-12-main.log : view postgres logs
adduser fastapi-tutorial : add user to virtual maching
usermod -aG sudo fastapi-tutorial : modify user permission
mkdir app : create app directory
virtualenv venv : install virtualenv
source venv/bin/activate : activate virtual environment
mkdir src : create a directory call source
git clone {giturl} : clone git url into source folder
pip install -r requirments.txt : to install all requirements
set -o allexport; source /home/fastapi-tutorial/.env; set +o allexport : set all environment variables. 
alembic upgrade head : Alembic upgrade head
uvicorn --host 0.0.0.0 app.main:app: specify host for uvicorn
unicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000 : use gunicorn to specify number of workers for load balancing
systemctl restart fastapi : start services
systemctl status fastapi : check on services
sudo apt install nginx -y: installing nginx to handle https request and request forwarding to the our api server 
cd /etc/nginx/sites-available : got to that directory, edit the default file, on the location and add the configue on the nginx file
systemctl restart nginx
go to namecheap create domain, 
after set up look at video to configure website to domain
go to this site to enable ssl: https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal
sudo ufw allow http: configure firewall to allow http
sudo ufw allow https: configure firewall to all https
sudo ufw allow ssh: configure firewall to allow ssh
sudo ufw allow 5432: configure to allow postgres traffic | not recomended
sudo ufw delete allow http: delete a rule



