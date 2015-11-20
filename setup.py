import io
import os
import re
from setuptools import setup, find_packages

def read(*names, **kwargs):
    with io.open(
            os.path.join(os.path.dirname(__file__), *names),
            encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")



setup(
    name='django_auth_ldap3_ad_backend',
    version=find_version('django_auth_ldap3_ad_backend', '__init__.py'),
    description='Django authenticate backend for Windows Active Directory with LDAP3 library',
    long_description='Django authenticate backend for Windows Active Directory with LDAP3 library',
    url='https://github.com/thinkAmi/django-auth-ldap3-ad-backend',
    author='thinkAmi',
    author_email='dev.thinkami@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='django auth backend ldap activedirectory',
    packages=find_packages(exclude=['test*']),
    install_requires=[
        'ldap3>=0.9.9',
        'django>=1.8'
    ],
)