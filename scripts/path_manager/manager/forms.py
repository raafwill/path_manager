from django import forms
import os
import glob
paths = glob.glob("C:/Users/willi/Desktop/PDFS-TESTES/*")
paths2 = glob.glob("C:/Users/willi/Desktop/PDFS-ORG/*")
list_paths = []
list_paths_to_upload = []

class Manage(forms.Form):
    count = 0
    for p in paths:
        list_paths.append((count, p))
        count +=1

    for p in paths2:
        list_paths_to_upload.append((count, p))
        count +=1

    print(list_paths)
    excel = forms.FileField()
    path = forms.ChoiceField(choices=list_paths)
    path_to_upload = forms.ChoiceField(choices=list_paths_to_upload)