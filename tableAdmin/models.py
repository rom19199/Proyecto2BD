from django.db import models

class Music(models.Model):  
    name = models.CharField(max_length=100)  
    album = models.CharField(max_length=100)  
    artista = models.CharField(max_length=100)  
    year = models.CharField(max_length=100)  
    genero = models.CharField(max_length=100)  
  
    class Meta:  
        db_table = "songsadmin"
        # app_label="Proyecto2"