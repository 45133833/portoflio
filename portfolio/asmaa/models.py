from django.db import models

class About(models.Model):
    heading=models.CharField(max_length=50)
    carrer=models.CharField(max_length=50)
    description=models.CharField(max_length=520)
    profile_img=models.ImageField(upload_to='media/')
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.carrer

class Home(models.Model):
    name=models.CharField(max_length=50)
    text1=models.CharField(max_length=50)
    text2=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/')
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.name
    
    

    
class Profile(models.Model):
    about=models.ForeignKey(About, on_delete=models.CASCADE)
    social_name=models.CharField(max_length=55)
    link=models.URLField(max_length=200)

#static section

class Category(models.Model):
    name=models.CharField(max_length=50)
    time=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    def __str__(self) :
        return self.name


class skills(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=50)
    



class Portfolio(models.Model):
    img=models.ImageField(upload_to='media/')
    link=models.URLField(max_length=200)

    def __str__(self) :
        return f"portfolio {self.id}"

    