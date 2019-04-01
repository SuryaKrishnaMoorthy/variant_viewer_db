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

import vviewer
uri = 'postgresql+psycopg2://postgres@localhost:5432/postgres'
from ngsdb.schemas import orm
db = orm.init_db(uri)
s1 = orm.Samples(id=1, tissue_type="heart", tumor_sample=True)
s2 = orm.Samples(id=2, tissue_type="lungs", tumor_sample=True)
db.add(s1)
db.add(s2)
db.commit()
s1@s2 => will run **matmul**

<!-- Post Source -->

curl -d '{"mrn": "Mr", "first_name": "John", "last_name": "Doe", "gender": "Male", "dob": "1990-12-19 09:26:03.47803", "maternal_id": 1, "paternal_id": 1, "family_id": 1, "permissions": "{test-permission: True}", "created_by": "source testname"}' -H "Content-Type: application/json" -X POST http://localhost:5000/sources

curl -d '{"mrn": "Ms", "first_name": "Jane", "last_name": "Doe", "gender": "Female", "dob": "1990-12-19 09:26:03.47803", "maternal_id": 1, "paternal_id": 1, "family_id": 1, "permissions": "{test-permission: True}", "created_by": "source testname"}' -H "Content-Type: application/json" -X POST http://localhost:5000/sources

<!-- Delete Sample -->

curl -X DELETE 'http://localhost:5000/sources/1'

<!-- Post Sample -->

curl -d '{ "tissue_type": "liver", "tumor_sample": false, "date_collected": "2018-12-19 09:26:03.47803","date_used": "2018-12-19 09:26:03.47803", "source_id":1, "phenotype": "{resourceType: Observation,id: example-phenotype}","permissions": "{test-permission: True}", "created_by": "testname"}' -H "Content-Type: application/json" -X POST http://localhost:5000/samples

<!-- Delete Sample -->

curl -X DELETE 'http://localhost:5000/samples/1'

<!-- Post Study -->

curl -d '{ "permissions": "{test-permission: True}", "source_id": 1}' -H "Content-Type: application/json" -X POST http://localhost:5000/studies

<!-- Delete Study -->

curl -X DELETE 'http://localhost:5000/studies/1'
