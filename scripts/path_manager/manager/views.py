from django.shortcuts import render, redirect
from .forms import Manage
import pathlib
import glob
import pandas as pd
from manager.exe.reader import PathManager 
from .models import Reader
from django.views.generic import ListView, DetailView, View


def manage(request):
    form = Manage(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/readers-list')
    
    context = {"form": form, "title": "Criar Nova Ordem"}

    return render(request, "manage.html", context)


def pdf_reader(request, pk):
    reading = Reader.objects.get(id=pk)
    excel = "C:/Users/willi/Desktop/PDFS-ORG/NOTAS.xlsx"
    path = reading.path_files
    new_path = reading.path_to_manage

    return render(request, {"read": PathManager.read(path, excel, new_path)})


class Readers_list(ListView):
        template_name = 'readers-list.html'
        model = Reader
        paginate_by = 20

        def get_queryset(self):
            p = Reader.objects.filter(status="Criado")
            return p