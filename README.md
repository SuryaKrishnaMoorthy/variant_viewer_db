# Example Python Project

## Project Structure

    .
    ├── README.md
    ├── cliapp
    │   ├── __init__.py
    │   ├── commands
    │   │   ├── __init__.py
    │   │   └── uniprot.py
    │   └── runner.py
    └── setup.py

## Parts of a Project

1. README.md

   The elevator pitch for your application/library! You should include info
   about the purpose of your project, installation instructions, and some
   examples or quick start vignettes.

2. cliapp

   Your Python package, this directory/folder usually has the same name as your
   application/library and contains your source code.

3. setup.py

   This python module/file/script allows pip, Python's package manager, to
   install your project. It stores the specific dependency requirements of
   your application.

4. **init**.py

   This file, often empty, is how Python decides a directory/folder is a
   Python package.

## Installation

pip install -e git+git://github.com/JHibbard/pyclass2019.git

## Deploying Test Instance

1. CleanUp

   0a docker stack ls
   0b remove unwanted service stack - docker stack rm service_name

1. If you haven't already pull postgres image from Dockerhub
   docker pull postgres
1. deploy service stack
   docker stack deploy -c docker-compose.yaml sqla
1. connect to database, create missing tables
   3a. enter python interactive terminal
   3b. import orm
   3c. use init_db function to connect
   e.g. uri for sqlalchemy:
   uri = 'postgresql+psycopg2://postgres@localhost:5432/postgres'
   db = orm.init_db(uri)

# example of inserting into db:

> > > sample = orm.Sample(type='skin')
> > > db.add(sample)
> > > db.commit()
> > > sample.id
