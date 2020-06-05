from setuptools import setup, find_packages

setup (
  name                 = "todobackend",
  version              = "0.1.0",
  description          = "Todobackend Django REST service",
  packages             = find_packages(),
  include_package_data = True, 
  scripts              = ["manage.py"], 
  install_requires     = ["asn1crypto==0.24.0",
			  "certifi==2018.11.29",
			  "cffi==1.11.5",
			  "chardet==3.0.4",
			  "conda==4.3.16",
			  "configparser==3.7.4",
			  "cryptography==2.4.2",
			  "Django==2.2.13",
			  "django-cors-headers==2.5.2",
			  "djangorestframework==3.9.2",
			  "idna==2.8",
			  "pycosat==0.6.3",
			  "pycparser==2.19",
			  "PyMySQL==0.9.3",
			  "pyOpenSSL==18.0.0",
			  "PySocks==1.6.8",
			  "pytz==2018.9",
			  "requests==2.21.0",
			  "ruamel-yaml==0.15.94",
			  "six==1.12.0",
			  "urllib3==1.24",
			  "virtualenv==16.4.3",
			  "uwsgi==2.0.17.1"],
  extras_require       = {
                            "test": [
                              "colorama>=0.4.1",
                              "coverage>=4.5.3",
                              "django-nose>=1.4.6",
                              "nose>=1.3.7",
                              "pinocchio>=0.4.2"
                            ]
                         }
)
