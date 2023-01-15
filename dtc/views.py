from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings
from .forms import DataForm
from .models import Data

# Ekspor CSV/Excel
from .resource import PasienResource

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def dtc(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        dtc_test = Data.objects.filter(name__contains=kata_kunci)
        context = {
            'page_title': 'Data Pasien',
            'dtc_test': dtc_test,
        }
    else:
        dtc_test = Data.objects.all()
        context = {
            'dtc_test': dtc_test
        }
    return render(request, 'dtc/prediksidtc.html', context)


@login_required(login_url=settings.LOGIN_URL)
def prediksidtc(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil di Prediksi")
            return redirect('dtc:dtc')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'dtc/testdtc.html', context)


@login_required(login_url=settings.LOGIN_URL)
def hapus(request, delete_id):
    Data.objects.filter(id=delete_id).delete()
    messages.success(request, "Data Berhasil di Hapus")
    return redirect('dtc:dtc')


@login_required(login_url=settings.LOGIN_URL)
def prediksidtc2(request):
    context = {
        'page_title': 'dtc',
    }
    return render(request, 'dtc/dtc.html', context)


@login_required(login_url=settings.LOGIN_URL)
def resultdtc(request):
    # untuk memisahkan data training dan testing
    from sklearn.model_selection import train_test_split

    # Pengujian Confusion Matrix
    from sklearn.metrics import confusion_matrix

    # Plot
    import seaborn as seabornInstance

    # untuk mengetahui skor
    from sklearn.metrics import accuracy_score

    # untuk evaluasi model
    from sklearn.metrics import classification_report

    # untuk dataframe
    import pandas as pd

    # untuk model C4.5
    from sklearn.tree import DecisionTreeClassifier

    # untuk memasukan data
    dataset = pd.read_csv(r"D:\Projek_Python\ta2\dkp\media\files\excels\data.csv")

    # melakukan Feature Scaling
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    dataset.columns

    scaler.fit(dataset[['Radius_mean', 'Texture_mean',
                        'Perimeter_mean', 'Area_mean', 'Smoothness_mean', 'Compactness_mean',
                        'Concavity_mean', 'Concave_points_mean', 'Symmetry_mean',
                        'Fractal_dimension_mean', 'Radius_se', 'Texture_se', 'Perimeter_se',
                        'Area_se', 'Smoothness_se', 'Compactness_se', 'Concavity_se',
                        'Concave_points_se', 'Symmetry_se', 'Fractal_dimension_se',
                        'Radius_worst', 'Texture_worst', 'Perimeter_worst', 'Area_worst',
                        'Smoothness_worst', 'Compactness_worst', 'Concavity_worst',
                        'Concave_points_worst', 'Symmetry_worst', 'Fractal_dimension_worst']])

    transformed = scaler.transform(dataset[['Radius_mean', 'Texture_mean',
                                            'Perimeter_mean', 'Area_mean', 'Smoothness_mean', 'Compactness_mean',
                                            'Concavity_mean', 'Concave_points_mean', 'Symmetry_mean',
                                            'Fractal_dimension_mean', 'Radius_se', 'Texture_se', 'Perimeter_se',
                                            'Area_se', 'Smoothness_se', 'Compactness_se', 'Concavity_se',
                                            'Concave_points_se', 'Symmetry_se', 'Fractal_dimension_se',
                                            'Radius_worst', 'Texture_worst', 'Perimeter_worst', 'Area_worst',
                                            'Smoothness_worst', 'Compactness_worst', 'Concavity_worst',
                                            'Concave_points_worst', 'Symmetry_worst', 'Fractal_dimension_worst']])

    toMakeNewDataFrame = dataset[['Radius_mean', 'Texture_mean',
                                  'Perimeter_mean', 'Area_mean', 'Smoothness_mean', 'Compactness_mean',
                                  'Concavity_mean', 'Concave_points_mean', 'Symmetry_mean',
                                  'Fractal_dimension_mean', 'Radius_se', 'Texture_se', 'Perimeter_se',
                                  'Area_se', 'Smoothness_se', 'Compactness_se', 'Concavity_se',
                                  'Concave_points_se', 'Symmetry_se', 'Fractal_dimension_se',
                                  'Radius_worst', 'Texture_worst', 'Perimeter_worst', 'Area_worst',
                                  'Smoothness_worst', 'Compactness_worst', 'Concavity_worst',
                                  'Concave_points_worst', 'Symmetry_worst', 'Fractal_dimension_worst']]

    fc = pd.DataFrame(transformed, columns=toMakeNewDataFrame.columns)

    # untuk memisahkan data training dan testing
    # X_train = data train
    # X_test = data testing
    # y_train = label train
    # y_test = label test
    X_train, X_test, y_train, y_test = train_test_split(fc, dataset
    ['Diagnosis'],
                                                        test_size=0.30,
                                                        random_state=42)

    # Mangaktifkan C4.5
    dcModel = DecisionTreeClassifier(criterion='entropy')

    dcModel.fit(X_train, y_train)

    dcModel.fit(X_train, y_train)

    lis = []

    lis.append(request.GET['Radius_mean'])
    lis.append(request.GET['Texture_mean'])
    lis.append(request.GET['Perimeter_mean'])
    lis.append(request.GET['Area_mean'])
    lis.append(request.GET['Smoothness_mean'])
    lis.append(request.GET['Compactness_mean'])
    lis.append(request.GET['Concavity_mean'])
    lis.append(request.GET['Concave_points_mean'])
    lis.append(request.GET['Symmetry_mean'])
    lis.append(request.GET['Fractal_dimension_mean'])

    lis.append(request.GET["Radius_se"])
    lis.append(request.GET['Texture_se'])
    lis.append(request.GET['Perimeter_se'])
    lis.append(request.GET['Area_se'])
    lis.append(request.GET['Smoothness_se'])
    lis.append(request.GET['Compactness_se'])
    lis.append(request.GET['Concavity_se'])
    lis.append(request.GET['Concave_points_se'])
    lis.append(request.GET['Symmetry_se'])
    lis.append(request.GET['Fractal_dimension_se'])

    lis.append(request.GET["Radius_worst"])
    lis.append(request.GET['Texture_worst'])
    lis.append(request.GET['Perimeter_worst'])
    lis.append(request.GET['Area_worst'])
    lis.append(request.GET['Smoothness_worst'])
    lis.append(request.GET['Compactness_worst'])
    lis.append(request.GET['Concavity_worst'])
    lis.append(request.GET['Concave_points_worst'])
    lis.append(request.GET['Symmetry_worst'])
    lis.append(request.GET['Fractal_dimension_worst'])

    # print(lis)
    pred = dcModel.predict([lis])

    return render(request, 'dtc/resultdtc.html', {'pred': pred, 'lis': lis})

login_required(login_url=settings.LOGIN_URL)
def export_csv(request):
    pasien = PasienResource()
    Data = pasien.export()
    response = HttpResponse(Data.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=datac4.5.csv'
    return response

@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    pasien = PasienResource()
    Data = pasien.export()
    response = HttpResponse(Data.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=datac4.5.xls'
    return response
