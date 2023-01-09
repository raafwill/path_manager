import PyPDF2
import re
import os 
import zipfile
import shutil
import copy
import pathlib
import pandas as pd
import glob

path = "C:/Users/willi/Desktop/PDFS-TESTES/"
dir = "C:/Users/willi/Desktop/PDFS-ORG/"
excel_file = "C:/Users/willi/Desktop/PDFS-ORG/mcm.xlsx"

mydict = {}
new_dict = {}
count = 0
text = ""
loop = 0

def create_one(mydict, new_dict):
    new_dict["codigo de verificação"] = [mydict[2]]
    new_dict["DATA E HORA DA EMISSÃO"] = [mydict[4]]
    new_dict["IBGE"] = [mydict[5]]
    new_dict["Nº RPS SUBSTITUIDO"] = [mydict[7]]
    new_dict["SIAFI"] = [mydict[9]]
    new_dict["SERVIÇO PRESTADO NO MUNICÍPIO"] = [mydict[12]]
    new_dict["IE"] = [mydict[33]]
    new_dict["DESCRIÇÃO DO SERVIÇO"] = [descricao_servico]
    new_dict["VALOR TOTAL DOS SERVIÇOS"] = [mydict[38+dif]]
    new_dict["PIS"] = [mydict[41+dif]]
    new_dict["COFINS"] = [mydict[43+dif]]
    new_dict["INSS"] = [mydict[45+dif]]
    new_dict["IR"] = [mydict[47+dif]]
    new_dict["CSLL"] = [mydict[49+dif]]
    new_dict["Valor ISS"] = [mydict[51+dif]]
    new_dict["Alíquota ISS"] = [mydict[53+dif]]
    new_dict["Base de Cálculo"] = [mydict[55+dif]]
    new_dict["SERVIÇO"] = [mydict[57+dif]]
    new_dict["VALOR LÍQUIDO DA NFS-e"] = [mydict[58+dif]]
    
def create_two(mydict, new_dict):
    new_dict["codigo de verificação"].append(mydict[2])
    new_dict["DATA E HORA DA EMISSÃO"].append(mydict[4])
    new_dict["IBGE"].append(mydict[5])
    new_dict["Nº RPS SUBSTITUIDO"].append(mydict[7])
    new_dict["SIAFI"].append(mydict[9])
    new_dict["SERVIÇO PRESTADO NO MUNICÍPIO"].append(mydict[12])
    new_dict["IE"].append(mydict[33])
    new_dict["DESCRIÇÃO DO SERVIÇO"].append(descricao_servico)
    new_dict["VALOR TOTAL DOS SERVIÇOS"].append(mydict[38+dif])
    new_dict["PIS"].append(mydict[41+dif])
    new_dict["COFINS"].append(mydict[43+dif])
    new_dict["INSS"].append(mydict[45+dif])
    new_dict["IR"].append(mydict[47+dif])
    new_dict["CSLL"].append(mydict[49+dif])
    new_dict["Valor ISS"].append(mydict[51+dif])
    new_dict["Alíquota ISS"].append(mydict[53+dif])
    new_dict["Base de Cálculo"].append(mydict[55+dif])
    new_dict["SERVIÇO"].append(mydict[57+dif])
    new_dict["VALOR LÍQUIDO DA NFS-e"].append(mydict[58+dif])

#loop for read each file
for i in os.listdir(path):
    loop+=1    
    pdfFileObj = open(path+i, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    info=pdfReader.getDocumentInfo()
    print(info)

    while count < 1:
        pageObj = pdfReader.getPage(1)
        count +=1
        text = text + pageObj.extractText()

    pdfFileObj.close()

    with open("C:/Users/willi/Desktop/PDFS-ORG/readme.txt", 'w') as f:
        f.write(text)

    with open('C:/Users/willi/Desktop/PDFS-ORG/readme.txt', 'r') as d:
        rows = d.read().splitlines()

    
    lines = range(len(rows))

    for l in lines:
        mydict[l]= rows[l]
    

    a = {i for i in mydict if mydict[i]=='RODOVIA BR-010, 1503'}
    a = list(a)
    b = {i for i in mydict if mydict[i]=='DESCRIÇÃO DO SERVIÇO'}
    b = list(b)

    desc = abs(a[0]-b[0])-2

    if desc >0:
        dif = int(desc)
    else:
        dif = 0

    descricao_servico = ""
    for i in range(a[0]+1, b[0]):
        print(i)
        descricao_servico = descricao_servico + ", "+ mydict[i]

    if any(new_dict):
        create_two(mydict, new_dict)
    else:
        create_one(mydict, new_dict)
    
df = pd.DataFrame(new_dict)
df.to_excel(excel_file, sheet_name="teste", index=False)
print(df)
