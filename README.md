# README.md
    Simple application for Movie management.
##Setup virtual environment
    sudo apt-get install -y python3-pip

    sudo apt install python3-venv -y  && python3 -m venv venv && . venv/bin/activate
 
##Install requirments
    pip install -r requirments.txt
 

##Define environment variables
    export CREDY_MOVIE_API_USERNAME='<username>'
    export CREDY_MOVIE_API_PASSWORD='<password>'
    export DATABASE_NAME='<database_name>'
    export USERNAME='<database_username>'
    export PASSWORD='<databse_password>'
 ##Run Migration
    python manage.py makemigrations

    python manage.py migrate
 
 ##Run Application
    python manage.py runserver
    