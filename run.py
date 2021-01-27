import pandas as pd
from docxtpl import DocxTemplate
import re

excel = pd.read_excel(r"C:\Users\Leo\Documents\Lu\planilha.xlsx")

def run(n):
    try: 
        tpl = DocxTemplate("template.docx")
        cnpj = str(excel['CNPJ'][n])
        cnpj = re.sub('[^0-9]', '', cnpj)
        cnpj = '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
        context = {n:{"CNPJ":cnpj, "Endereço":excel['ENDEREÇO'][n]}}
        cnpj = re.sub('[^0-9]', '', cnpj)
        cnpj = '{}.{}.{}.{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
        name = cnpj+" - Declarações"
        tpl.render(context[n])
        tpl.save("%s.docx" %name)
    except:
        print ("Erro ao criar arquivo Doc para o CNPJ: ",cnpj)
        

for i in range(0, 122):
    run(i)
