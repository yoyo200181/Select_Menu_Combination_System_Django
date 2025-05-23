from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Menu(models.Model):

    FOOD_TYPE = (
        ('MEAT', 'meat'),
        ('EGG', 'egg'),
        ('VEGETABLE', 'vegetable'),
        ('GRAIN', 'grain'),
        ('SET', 'set'),
    )
    name = models.CharField(max_length=100)
    kcal = models.IntegerField()
    protein = models.DecimalField(max_digits=3, decimal_places=1)
    fat = models.DecimalField(max_digits=3, decimal_places=1)
    carbs = models.DecimalField(max_digits=3, decimal_places=1)
    fiber = models.DecimalField(max_digits=3, decimal_places=1)
    salt = models.DecimalField(max_digits=3, decimal_places=1)
    image_url = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    type = models.CharField(max_length=10, choices=FOOD_TYPE, default=FOOD_TYPE[0][0])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"<Menu {self.name}>"
