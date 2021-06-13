from django.db import models


# TODO: Buscar como hacer un app.properties para guardar las configuraciones (upload_to)
class UserModel(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    email = models.EmailField()
    picture = models.ImageField(upload_to="./image/")
    birthday = models.DateField()
    password = models.CharField(max_length=256)
