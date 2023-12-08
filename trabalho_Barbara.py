import re
import time
from functools import reduce             
from collections import Counter  
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_PT')

def extrair_tags():
    #Regex para as tags, em que tudo o que se encontra a seguir a "tag:" dentro de chavetas é um match.
    tags = re.findall(r'tag:{?([\w\d \-\“\”\.\|\!\"\'\%\&\\\n\+\(\)\/]+)}', text)   
    return tags

def extrair_datas():
    #Regex para as datas, em que tudo o que se encontra a seguir a "#DATE: (qualquer texto) —" é um match.
    datas = re.findall(r'\#DATE\: \[[\w\d]+\] [\w\d ]+ \— ?([\w\d ]+)', text)
    return datas

#Converter datas para um formato genérico para se puder calcular a menor e a maior data 
def converter_para_datetime(data):
    return datetime.strptime(data, '%d de %B de %Y')

def extrair_etiquetas():
     #Regex para as etiquetas , em que tudo o que se encontra a seguir a "Etiquetas:" é um match.
    etiquetas = re.findall(r'Etiquetas: ?([\w\d ]+)', text)
    return etiquetas


#Abrir ficheiro                                        
text=open('folha8_OUT.txt',encoding="utf-8").read()

################### Contar o número de publicações ###################

#Contagem de publicações através da tag #DATE                                                                
numero_ocorrencias = text.count('#DATE')
print(f"Existem {numero_ocorrencias} publicações no documento.")  

################### Extrair e contar as tags existentes no ficheiro, colocando num ficheiro txt ###################
 
filtrar_tags=extrair_tags()

#Contagem do número de tags.
numero_tags=len(filtrar_tags)

time.sleep(1) # Sleep de 1 segundo

print("O número de tags é: " + str(numero_tags))

filtrar_tags_distintas=list(set(filtrar_tags))

#Contagem do número de tags distintas.
numero_tags_distintas=len(filtrar_tags_distintas)

time.sleep(1) # Sleep de 1 segundo

print("O número de tags distintas é: " + str(numero_tags_distintas))

#Contagem do número de ocorrências das tags 
contar_tags = Counter(filtrar_tags)                         

#Passagem do resultado para um documento txt
with open('contagem_tags.txt', 'w') as file:                
    for tag, ocorrencia in contar_tags.items():
        file.write(f'{tag}: {ocorrencia}\n')



################### Gamas de datas incluidas (quando uma data começa e acaba) e o seu respetivo número, colocando num ficheiro txt ###################

filtrar_datas=extrair_datas()

#Contagem do número de datas.
numero_datas=len(filtrar_datas)

time.sleep(1) # Sleep de 1 segundo

print("O número de datas é: " + str(numero_datas))

datas_convertidas = [converter_para_datetime(data) for data in filtrar_datas]
menor_data = min(datas_convertidas)
maior_data = max(datas_convertidas)

time.sleep(1) # Sleep de 1 segundo

print(f"A gama de data está entre: {menor_data.strftime('%d de %B de %Y')} e {maior_data.strftime('%d de %B de %Y')}.")

#Contagem do número de ocorrências de datas
contar_datas = Counter(filtrar_datas)

#Passagem do resultado para um documento txt
with open('contagem_datas.txt', 'w') as file:
    for data, ocorrencia in contar_datas.items():
        file.write(f'{data}: {ocorrencia}\n')



################### Calcular o número de etiquetas e as mais comuns, colocando num ficheiro txt ###################

filtrar_etiquetas=extrair_etiquetas()

#Contagem do número de etiquetas.
numero_etiquetas=len(filtrar_etiquetas)

time.sleep(1) # Sleep de 1 segundo

print("O número de etiquetas é: " + str(numero_etiquetas))

#Contagem do número de ocorrências de etiquetas.
contar_etiquetas = Counter(filtrar_etiquetas)

#Passagem do resultado para um documento txt
with open('contagem_etiquetas.txt', 'w') as file:
    for etiqueta, ocorrencia in contar_etiquetas.items():
        file.write(f'{etiqueta}: {ocorrencia}\n')

print("\nTrabalho realizado por Bárbara Ribeiro")