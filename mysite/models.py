from django.db import models

#id по умолчанию(проверить)


class People(models.Model):
    name = models.CharField(max_length=40)
    salary = models.IntegerField("Salary")
    spend_now = models.IntegerField("Spend")


class Eat(models.Model):
    price = models.IntegerField()
    image = models.ImageField()
    #требует Pillow для пикчи