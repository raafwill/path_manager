from django.shortcuts import render
from .forms import Manage
import pathlib
import glob
import pandas as pd



def manage(request):
    context = {}
    context["form"]= Manage()

    return render(request, "manage.html", context)

def read_pdf()