comp3111project
===============
Repo for comp 3111

For feedback to run properly:

simply remove the CHUNK_SIZE import and add a 'try except' for the import à la:

try:
    from django.db.models.query import CHUNK_SIZE
except ImportError:
    CHUNK_SIZE = 100
    
    
Also replace the line "from django.conf.urls.defaults import patterns, url" in c:\python\lib\site-packages\hvad\admin.py with "from django.conf.urls import patterns, url, include"
