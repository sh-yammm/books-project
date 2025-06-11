from django.db import models

import uuid

# Create your models here.

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        abstract = True

class EditionChoices(models.IntegerChoices):

    ONE = 1 , '1'
    TWO = 2 , '2'
    THREE = 3 , '3'
    FOUR = 4 , '4'
    FIVE = 5 , '5'

class GenreChoices(models.TextChoices):

    FICTION = 'Fiction', 'Fiction'
    NON_FICTION = 'Non-Fiction', 'Non-Fiction'
    SCIENCE = 'Science', 'Science'
    HISTORY = 'History', 'History'
    FANTASY = 'Fantasy', 'Fantasy'
    MYSTERY = 'Mystery', 'Mystery'
    BIOGRAPHY = 'Biography', 'Biography'
    ROMANCE = 'Romance', 'Romance'
    THRILLER = 'Thriller', 'Thriller'

class Books(BaseClass):

    title = models.CharField(max_length=50)

    published_year =models.CharField(max_length=4)

    edition = models.IntegerField(choices=EditionChoices.choices)

    genre = models.CharField(max_length=20,choices=GenreChoices.choices)

    price = models.FloatField()

    offer_price = models.FloatField(null=True, blank=True)

    author = models.CharField(max_length=25)

    class Meta:

        verbose_name = 'Books'
        verbose_name_plural = 'Books'

    def __str__(self):

        return f'{self.title} - {self.author}'