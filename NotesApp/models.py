from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    """
    # | def __str__(self) -> str:
    #     return super().__str__()
    Creates 2 models and each Category class can have multiple Project values; w/ auto current date field and ForeignKey defined to tell DJ that each Proj is related to a single Category
    """
