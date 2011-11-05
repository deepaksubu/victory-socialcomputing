from django.db import models

class AppUser(models.Model):
      name = models.CharField(max_length=30)
      email = models.CharField(max_length=30)
      rating =models.IntegerField()
      def __utf8__(self):
          return self.name    

class Images(models.Model):
      name = models.CharField(max_length=30)
      location = models.CharField(max_length=300)
      rating = models.FloatField(null=True, blank=True) 
      def __utf8__(self):
          return self.name    

class Concepts(models.Model):
      name = models.CharField(max_length=30)
      description = models.CharField(max_length=300)
      def __utf8__(self):
          return self.name    

class Transaction(models.Model):
      user=models.ForeignKey(AppUser,verbose_name="user_id")
      image=models.ForeignKey(Images,verbose_name="image_id")
      concept=models.ForeignKey(Concepts,verbose_name="concept_id")
      location = models.CharField(max_length=300)




# Create your models here.
