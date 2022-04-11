from django.db import models
from django.forms import CharField




# Create your models here.
class Comments(models.Model):
    comments_id = models.AutoField(primary_key=True)
    post = models.TextField(max_length= 12000, default = 'No Comment')
   

class Recipes(models.Model):
    recipe_id = models.AutoField(primary_key= True)
    food_name = CharField(max_length= 400)
    ingredients = models.TextField(max_length=12000, default='Add Ingredients & Amount Here')
    instructions = models.TextField(max_length=12000, default ='Instruction/Meal Preps Go Here' )
    commenting = models.ManyToManyField(Comments)
    


