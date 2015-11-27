# django-auth-ldap3-ad-backend
Django authenticate backend for Microsoft Active Directory with LDAP3.

## Requirements
- Python 3.4
- Django 1.8
- LDAP3 0.9.9

## Setup 
### install

```
pip install git+https://github.com/thinkAmi/django-auth-ldap3-ad-backend.git
```

### Add `settings.py` to your Django app
#### INSTALLED_APPS

```python
INSTALLED_APPS = (
    ...
    'django_auth_ldap3_ad_backend',
)
```

#### AUTHENTICATION_BACKENDS

```python
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap3_ad_backend.backend.ADBackend',
)
```

#### django-auth-ldap3-ad-backend's settings
AD_DOAMIN_CONTROLLER_HOST_NAME is your domain controller host name or IP address (ex: 192.168.0.1).

```python
AD_DOAMIN_CONTROLLER_HOST_NAME = 'your_dc_host_name'
AD_DOMAIN_NAME = 'example.local'
```

## Usage Test Project

- clone or download this repo
- create virtualenv and activate
- pip install Django, LDAP3, django-auth-ldap3-ad-backend
  - Note: you want clone's django-auth-ldap3-ad-backend
    - `pip install -e path/to/django-auth-ldap3-ad-backend`
- update settings.py for your environment
- `python manage.py migrate`
- `python manage.py runserver`
- access to `http://localhost:8000/`

## Tested environment
- Windows10
- IntelliJ IDEA with Python plugin
- Python3.4.3
- Dango 1.8.6
- LDAP3 0.9.9.3
- Windows Server with Active Directory
  - On-premise or Azure Active Directory Domain Services(AADDS)

## License
MIT
