from django import forms
import os
import glob
paths = glob.glob("C:/Users/willi/Desktop/PDFS-ORG/*")
list_paths = []

class Manage(forms.Form):
    count = 0
    for p in paths:
        list_paths.append((count, p))
        count +=1
    print(list_paths)
    dir = forms.FilePathField(path="C:/Users/willi/Desktop/PDFS-ORG")
    path = forms.ChoiceField(choices=list_paths)