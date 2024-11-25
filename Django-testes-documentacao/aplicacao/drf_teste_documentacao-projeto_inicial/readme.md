python -m venv ./venv

cmd
venv\Scripts\activate.bat

powershell
.\venv\Scripts\Activate.ps1


pip install Django==3.1.5
python -m django --version
python -m django --version

pip install --upgrade djangorestframework

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser
 

pip install --upgrade django-filter

python manage.py runserver


## teste

python manage.py loaddata programas_iniciais.json