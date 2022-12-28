from django import forms
import os
import glob
from .models import Reader

class Manage(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ["user_exe", "excel_file", "path_to_manage", "path_files"]