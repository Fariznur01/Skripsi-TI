# Create your models here.
from django.db import models

# Create your models here.
class Basis(models.Model):
    Nama_Pasien = models.CharField(max_length=100)
    Tgl_Periksa = models.DateField(null=True)
    Diagnosis = models.CharField(max_length=40)
    #Mean
    Radius_mean = models.CharField(max_length=10)
    Texture_mean = models.CharField(max_length=10)
    Perimeter_mean = models.CharField(max_length=40)
    Area_mean = models.CharField(max_length=40)
    Smoothness_mean = models.CharField(max_length=40)
    Compactness_mean = models.CharField(max_length=40)
    Concavity_mean = models.CharField(max_length=40)
    Concave_points_mean = models.CharField(max_length=40)
    Symmetry_mean = models.CharField(max_length=40)
    Fractal_dimension_mean = models.CharField(max_length=40)
    #Se
    Radius_se = models.CharField(max_length=40)
    Texture_se = models.CharField(max_length=40)
    Perimeter_se = models.CharField(max_length=40)
    Area_se = models.CharField(max_length=40)
    Smoothness_se = models.CharField(max_length=40)
    Compactness_se = models.CharField(max_length=40)
    Concavity_se = models.CharField(max_length=40)
    Concave_points_se = models.CharField(max_length=40)
    Symmetry_se =models.CharField(max_length=40)
    Fractal_dimension_se = models.CharField(max_length=40)
    #Worst
    Radius_worst = models.CharField(max_length=40)
    Texture_worst = models.CharField(max_length=40)
    Perimeter_worst = models.CharField(max_length=40)
    Area_worst = models.CharField(max_length=40)
    Smoothness_worst = models.CharField(max_length=40)
    Compactness_worst = models.CharField(max_length=40)
    Concavity_worst = models.CharField(max_length=40)
    Concave_points_worst = models.CharField(max_length=40)
    Symmetry_worst = models.CharField(max_length=40)
    Fractal_dimension_worst = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.id)



