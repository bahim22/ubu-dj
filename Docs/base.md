# Django

> Begin by creating new dir, venv, and start the Django project and app

## Paths and views

- add the app name to projects _settings.py_ 'installed_apps'
- create view then register path inside _URLconf_
  - create view, then route, then register it in main proj _urls.py_
- route tells main proj what func to exe after a user req
    - paths are registered by config _urlpatterns_; which ID what DJ looks for in URL user req and what func handles it
    - the patterns are combined into the URLconf module.

1. add views(func/classes that exe a response after a user req; shows user html pages) to _views.py_ in app dir
2. create _urls.py _in app dir;
   1. map the views to the right URL/path
   2. the tuple connects/maps the views & URLS

## Models and Data

1. add Py classes to contain models in the apps _models.py_ file
2. register the app in INSTALLED_APPS list so DJ includes the app when the proj runs
   1. add config class name from the app dir apps.py file then add full path to class name in proj dir _settings.py_ file
- Object-relational mappers (`ORMs`): act as middleware between the app and DB.
  - Objects are made that model the data (including constraints and other forms of metadata). 
- Then the ORM: dynamically creates and updates the DB; handles queries; converts(maps) req made through the objects into the actual DB calls.

### Create models, add methods and fields and define field types and options, keys and relationships

1. `models`: representation of data that the app uses (define essential fields and behavior of the data)
2.  __str__ `method` used to display an object if no fields are specified.
3. `fields`: the data structure of a model (data the model stores)
   1. core metadata: the fields data type which are mapped to a DB type and HTML form control types
4. In relational DB, each row in table has a primary key (auto incremented int)
   1. auto in Dj ORM by adding id field
   2. RDB have relationships between tables
      1. `one-to-many`: foreign key relat. = multiple items share single attribute (e.g. many products grouped into a single category) 
         1. `ForeignKey` field added to child object.(e.g. If your products are grouped into categories, you add the category property to the Product class, and you set the type to be ForeignKey.)
         2. DJ auto adds prop to parent for accessing child objects (product_set)
         3. required param (on_delete): options:
            1. a. `CASCADE` = del all child objects (product) if a parent obj (category) is deleted
            2. b. `PROTECT` = returns err when trying to del a parent obj that contains child objects

    - `Field Types` = CharField: A single line of text, TextField: Multiple lines of text, BooleanField, DateField, TimeField, DateTimeField, URLField, IntegerField, DecimalField (fixed precision decimal number)
    - `Field Options`: used to add metadata that're mapped to the matching settings in the DB
    - min_length/max_length, min/max_value, auto_now (sets filed to current time on save(for last_update fields)), auto_now_add (set field to current time on creation (for creation_date fields))
    - `model`: class that gets it's functionality from django.models.Model
    - these collections have methods that enable: DB query, creating entries, saves & updates, define fields, set metadata,create relationships between models

```py
from django.db import models
class Product(models.Model):
    name = models.TextField(max_length=50, min_length=3, unique=True)
    price = models.DecimalField(min_value=0.99, max_value=1000)
    creation_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        'Category', # name of the model
        on_delete = models.PROTECT
    )

class Category(models.Model):
    name = models.TextField(max_length=50, min_length=3, unique=True)
    # product_set auto created
```

## Database management

1. use `migrations` proc to create/update the DB as models change
   1. collection of updates performed on the DB `schema`
      1. (def of the db itself; tables, columns, relations between tables)
      2. schema is defined by model creation

1. `makemigrations` cmd in manage.py uses the current list of migrations for a starting pt., then the current state of the models to determine the delta (changes that need to be made).(stores models as migrations) Then creates the required SQL to update the DB
   1. SQL statements can be built using `sqlmigrate`
2. `migrate` cmd exe all or specific migrations on DB, as configed in Proj _settings.py_
   1. can config diff DB conn str in DATABASES section of settings.py file
   2. Can display schema via cmd palette and use SQLite: Open Db to view DB tables & col. in VSC

```python
# app_label is name of your app (dir containing app)
# migration_name is name of migration
python manage.py migrate <app_label> <migration_name>

python manage.py showmigrations
python manage.py makemigrations 

python manage.py migrate
# cmd that runs our custom & DJ built in migrations 
```