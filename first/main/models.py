from django.db import models

class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    taskscompleted = models.ManyToManyField('Task', related_name='completed_by')

    def __str__(self):
        return self.nickname

class Task(models.Model):
    name = models.CharField(max_length=100)
    lvldifficulty = models.IntegerField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name
