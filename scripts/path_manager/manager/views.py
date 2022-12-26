from django.shortcuts import render
from .forms import Manage
import pathlib
import glob
import pandas as pd
from manager.exe.reader import PathManager 


def manage(request):
    form = Manage(request.POST or None)

    if form.is_valid():
        excel = form.cleaned_data.get('excel')
        path = form.cleaned_data.get('path')
        new_path = form.cleaned_data.get('path_to_upload')

        context = {"form": form,
                "title": "Criar Nova Ordem",
                }

        return render(request, "manage.html", context)
    
    context = {"form": form,
                "title": "Criar Nova Ordem",
                }
    return render(request, "manage.html", context)

def pdf_reader(request, excel, path, new_path):
    return render(request, {"read": PathManager.read(excel, path, new_path)})
