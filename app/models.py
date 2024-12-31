from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return self.name
    

class Goal(models.Model):
    CHOICE = [
        ("High", "Hight"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    STATUS = [
        ("Not Started", "Not started"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed")
    ]

    description = models.TextField()
    priority = models.CharField(max_length=50, choices=CHOICE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT, related_name="goals")
    status = models.CharField(max_length=50, choices=STATUS)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
