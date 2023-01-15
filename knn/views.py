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
def knn(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        knn_test = Data.objects.filter(name__contains=kata_kunci)
        context = {
            'page_title': 'Data Pasien',
            'knn_test': knn_test,
        }
    else:
        knn_test = Data.objects.all()
        context = {
            'knn_test': knn_test
        }
    return render(request, 'knn/prediksiknn.html', context)


@login_required(login_url=settings.LOGIN_URL)
def prediksiknn(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil di Prediksi")
            return redirect('knn:knn')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'knn/testknn.html', context)


@login_required(login_url=settings.LOGIN_URL)
def hapus(request, delete_id):
    Data.objects.filter(id=delete_id).delete()
    messages.success(request, "Data Berhasil di Hapus")
    return redirect('knn:knn')


@login_required(login_url=settings.LOGIN_URL)
def prediksiknn2(request):
    context = {
        'page_title': 'K-NN',
    }
    return render(request, 'knn/knn.html', context)


@login_required(login_url=settings.LOGIN_URL)
def result(request):
    # untuk memisahkan data training dan testing
    from sklearn.model_selection import train_test_split

    # untuk dataframe
    import pandas as pd

    # untuk model K-NN
    from sklearn.neighbors import KNeighborsClassifier

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
                                                        random_state=1)

    # Mengaktifkan K-NN
    knModel = KNeighborsClassifier(n_neighbors=11)
    # Jika KNN = 3  = 96
    # Jika KNN = 7  = 96
    # Jika KNN = 9  = 97
    # Jika KNN = 12 = 96
    # Jika KNN = 14 = 95
    # Jika KNN = 15 = 95

    knModel.fit(X_train, y_train)

    lis = []

    lis.append(request.GET["Radius_mean"])
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
    pred = knModel.predict([lis])

    return render(request, 'knn/result.html', {'pred': pred, 'lis': lis})

@login_required(login_url=settings.LOGIN_URL)
def export_csv(request):
    pasien = PasienResource()
    Data = pasien.export()
    response = HttpResponse(Data.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=datak-nn.csv'
    return response

@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    pasien = PasienResource()
    Data = pasien.export()
    response = HttpResponse(Data.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=datak-nn.xls'
    return response
