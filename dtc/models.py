from django.db import models
#from sklearn.tree import DecisionTreeClassifier

import joblib
# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)

    # Mean
    Radius_mean = models.CharField(max_length=100, null=True)
    Texture_mean = models.CharField(max_length=100, null=True)
    Perimeter_mean = models.CharField(max_length=100, null=True)
    Area_mean = models.CharField(max_length=100, null=True)
    Smoothness_mean = models.CharField(max_length=100, null=True)
    Compactness_mean = models.CharField(max_length=100, null=True)
    Concavity_mean = models.CharField(max_length=100, null=True)
    Concave_points_mean = models.CharField(max_length=100, null=True)
    Symmetry_mean = models.CharField(max_length=100, null=True)
    Fractal_dimension_mean = models.CharField(max_length=100, null=True)
    # Se
    Radius_se = models.CharField(max_length=100, null=True)
    Texture_se = models.CharField(max_length=100, null=True)
    Perimeter_se = models.CharField(max_length=100, null=True)
    Area_se = models.CharField(max_length=100, null=True)
    Smoothness_se = models.CharField(max_length=100, null=True)
    Compactness_se =models.CharField(max_length=100, null=True)
    Concavity_se = models.CharField(max_length=100, null=True)
    Concave_points_se = models.CharField(max_length=100, null=True)
    Symmetry_se = models.CharField(max_length=100, null=True)
    Fractal_dimension_se = models.CharField(max_length=100, null=True)
    # Worst
    Radius_worst = models.CharField(max_length=100, null=True)
    Texture_worst = models.CharField(max_length=100, null=True)
    Perimeter_worst = models.CharField(max_length=100, null=True)
    Area_worst = models.CharField(max_length=100, null=True)
    Smoothness_worst = models.CharField(max_length=100, null=True)
    Compactness_worst = models.CharField(max_length=100, null=True)
    Concavity_worst = models.CharField(max_length=100, null=True)
    Concave_points_worst = models.CharField(max_length=100, null=True)
    Symmetry_worst = models.CharField(max_length=100, null=True)
    Fractal_dimension_worst = models.CharField(max_length=100, null=True)

    predictions = models.CharField(max_length=100, blank=True)


    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_model_dkp02')
        self.predictions = ml_model.predict(
            [[self.Radius_mean, self.Texture_mean,
              self.Perimeter_mean, self.Area_mean, self.Smoothness_mean, self.Compactness_mean,
              self.Concavity_mean, self.Concave_points_mean, self.Symmetry_mean,
              self.Fractal_dimension_mean, self.Radius_se, self.Texture_se,
              self.Perimeter_se, self.Area_se, self.Smoothness_se, self.Compactness_se,
              self.Concavity_se, self.Concave_points_se, self.Symmetry_se,
              self.Fractal_dimension_se, self.Radius_worst, self.Texture_worst,
              self.Perimeter_worst, self.Area_worst, self.Smoothness_worst, self.Compactness_worst,
              self.Concavity_worst, self.Concave_points_worst, self.Symmetry_worst,
              self.Fractal_dimension_worst,]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name