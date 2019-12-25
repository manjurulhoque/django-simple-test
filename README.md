### Key Value store


##### Get values
``
/values
``

##### Get one or more specific values from the store
``
/values?keys=key1,key2
``

##### Save value to store with key
``
/values
``
and pass data like below
``
{key1: value1, key2: value2}
``

##### Update values
``
/values
``

and pass data like below
``
{key1: value1, key2: value2}
``

### Testing
run
``
python manage.py test
``