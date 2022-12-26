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
df = pd.read_excel("C:/Users/willi/Desktop/PDFS-ORG/NOTAS.xlsx")


class PathManager:

    def excel_file_df(excel):
        df = pd.read_excel(excel)
        return df

    def read(path, excel, npath):
        count = 0
        text = ""
        loop = 0
        #loop for read each file
        for i in os.listdir(path):
            loop+=1    
            print(i)
            pdfFileObj = open(path+i, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            num_pages = pdfReader.numPages
            info=pdfReader.getDocumentInfo()
            print(info)

            while count < num_pages:
                pageObj = pdfReader.getPage(count)
                count +=1
                text = pageObj.extractText()
                print("numero da pagina: ", count)

            pdfFileObj.close()

            with open(path+"/readme.txt", 'w') as f:
                f.write(text)

            with open(path+'/readme.txt', 'r') as d:
                rows = d.read().splitlines()

            mydict = {}
            lines = range(len(rows))

            for l in lines:
                mydict[l]= rows[l]
            print(mydict[5])
            serie = mydict[5]
            no_serie = re.findall(r"\d+", serie)
            no_serie = no_serie[0]

            print("esse é o numero de serie: ", no_serie)
            df = PathManager.excel_file_df(excel) #chamando função para transformar excel em dataframe

            no_servico = df.loc[df["NUMERO_DE_SERIE"] == int(no_serie), 'NUMERO_DO_SERVICO'].iloc[0]
            print("esse é o numero de serie: ", no_servico)

            #criando pastas para os arquivos
            new_path = os.path.join(npath, str(no_serie)+" - "+str(no_servico)+" - "+str(loop))
            print(new_path+i)
            os.makedirs(new_path)
            shutil.move(path+i, new_path+"/"+i)