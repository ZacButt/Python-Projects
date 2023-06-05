from django.db import models

class UniversityCampusManager(models.Manager):
    pass

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=2, default="")
    campus_id = models.IntegerField(default=0)

    objects = UniversityCampusManager()

    class Meta:
        verbose_name_plural = "University Campuses"

    def __str__(self):
        return self.campus_name

#class UniversityCampus(models.Model):
    # attributes and methods ..
    #class Meta:
       # verbose_name_plural = "University Campuses"
