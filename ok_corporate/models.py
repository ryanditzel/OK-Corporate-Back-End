from dataclasses import fields
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])

    def __str__(self):
        return self.name


class User(AbstractUser):

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


class CompanyReview(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
