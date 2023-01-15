from django import forms

from .models import  Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = [
        'name',
        'Radius_mean',
        'Texture_mean',
        'Perimeter_mean',
        'Area_mean',
        'Smoothness_mean',
        'Compactness_mean',
        'Concavity_mean',
        'Concave_points_mean',
        'Symmetry_mean',
        'Fractal_dimension_mean',
        # Se
        'Radius_se',
        'Texture_se',
        'Perimeter_se',
        'Area_se',
        'Smoothness_se',
        'Compactness_se',
        'Concavity_se',
        'Concave_points_se',
        'Symmetry_se',
        'Fractal_dimension_se',
        #worst
        'Radius_worst',
        'Texture_worst',
        'Perimeter_worst',
        'Area_worst',
        'Smoothness_worst',
        'Compactness_worst',
        'Concavity_worst',
        'Concave_points_worst',
        'Symmetry_worst',
        'Fractal_dimension_worst',
        ]





