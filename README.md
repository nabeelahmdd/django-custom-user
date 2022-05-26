# Django Custom User With allauth

```
A Django Website in which include custom 
user model with django-allauth setup and email setup also
template are available in bootstrap 5.
```

`` Authentication Supported Services ``
* Google
* Facebook
* Email & Password With Verification

## Usage

First clone this repo
```bash
git clone https://github.com/nabeelahmdd/django-custom-user.git 
```

Create A virtualenv
```bash
virtualenv env
```

Activate virtualenv
```bash
source env/bin/activate
```

Install Requirements
```bash
pip3 install -r requirements.txt
```

Create a `.env` file
```bash
touch mysite/.env
```


Place your credentials in `.env` file
```bash
SECRET_KEY=your-secret-key
EMAIL_HOST=your-email-host
EMAIL_HOST_USER=your-host-user
EMAIL_HOST_PASSWORD=your-host-password
```

Run Server
```bash
python3 manage.py runserver
```
