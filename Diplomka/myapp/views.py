from django.shortcuts import render, HttpResponse
from . import fileprocessing
import csv


def home(request):
    if request.method =="POST":
        time_array = []
        acc_array = []
        fft_array = []
        f_array = []
        #TODO: UDELAT OCHRANU PROTI VICE SOUBORUM ROZDELENI NA LEVOU PRAVOu
        for f in request.FILES.getlist('file'):
            time,acc,fft,f = fileprocessing.file_read(f)
            time_array.append(time)
            acc_array.append(acc)
            fft_array.append(fft)
            f_array.append(f)

        data ={
            "time_L": time_array[0],
            "time_R": time_array[1],
            "acc_L": acc_array[0],
            "acc_R": acc_array[1],
            "fft_L": fft_array[0],
            "fft_R": fft_array[1],
            "f_L": f_array[0],
            "f_R": f_array[1]
        }
        return render(request,"results.html",data)
    else:
        return render(request,"home.html")


def help(request):
    return render(request, "help.html")


def export_csv(request):
    # Your data retrieval logic goes here
    data = [
        ['Name', 'Age', 'Email'],
        ['John Doe', 30, 'john@example.com'],
        ['Jane Smith', 25, 'jane@example.com'],
        # Add your data here
    ]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'

    writer = csv.writer(response)
    for row in data:
        writer.writerow(row)

    return response

# Create your views here.
