# GDP-Bar-Charts


# Introduction

While most demographers and economists have viewed socioeconomic factors as the driving forces behind fertility decline in developing countries, there is growing evidence that the “ease” of access to, or realistic availability of, fertility regulation methods may be at least as important in this demographic change. Much of the world's fertility decline has occurred where fertility regulation methods are relatively easy to obtain regardless of a "program", and those countries have not all exhibited economic development or significant improvements in education before the decline. In addition, there is evidence that removing barriers to family planning options actually builds a desire for small families – which would be consistent with our consumer behavior regarding other products and services. If governments and international donor agencies recognize and move to reduce certain barriers, this will benefit parents by enabling them to achieve their family size goals, and improve maternal health and child survival.

This webapp provides a visualization of data showing that some countries have reduced family size before economic development has increased while also showing that most countries with fertility above replacement level have economies that are less developed.


### 

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Procfile for easy deployments

* Separated requirements files

* SQLite by default if no env variable is set

# Usage

To use this template to start your own project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ project_name|title }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
