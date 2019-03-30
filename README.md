<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django-2.0.7 project." title="A Django project." /></a>
# Optimal Route Identifier API
**__A django-rest-api repository which provide following featues:__**
```bash
 1. CRUD for grid/route. (Make sure all nodes are connected)

 2. Find the optimal distance between two given node based on the distance and speed factor.
```

#### Solution
> Make a weighted graph with all the given edges and assinged the weight as distance between nodes and speed.
  To find the optimal route between two points/nodes, we need to find the all posssible path by the formula \
  (Σ distance/speed) and then we need to find the smallest value path as an Optimal path.

#### Setup
**RUN:**
```bash
$ .setup/setup.sh
```

**UPDATE the .env file, Make the following changes**

> Update Mongo credentials

#### Start Application 

```bash
    $ ./start.sh
```
> OR
```bash
    $ source venv/bin/activate
    $ supervisorctl -c supervisord.conf start all
```

#### Stop Application
```bash
    $ ./start.sh
```
> OR
```bash
    $ source venv/bin/activate
    $ supervisorctl -c supervisord.conf stop all
```

#### Restart Application
```bash
    $ ./restart.sh
```

#### Endpoints

> use postman file ``` Optimal-Route-Identifier.postman_collection.json``` for endpoint and schema info.

