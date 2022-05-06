from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return self.name


class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Review(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=50)
    jobtitle = models.CharField(max_length=100)
    body = models.TextField()
    helpful = models.IntegerField(default=0)
    unhelpful = models.IntegerField(default=0)

    def __str__(self):
        return self.title
