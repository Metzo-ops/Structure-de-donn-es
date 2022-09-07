from asyncore import write
import csv
from fileinput import filename
from nis import match


def transform_json_en_csv() :
    import json
# je veux ouvrir ma page json comme dictionaire
    with open("page0.json") as file:
        page = json.load(file)
#        print(page) 
# maintenant, je veux convertir mon dictionnaire en fichier csv         
        with open ("lex.csv", "w") as csv_file:
            for key in page.keys():
                csv_file.write("%s, %s\n" % (key, page[key])) 
        with open("lex.csv", "r") as read_csv_file:
            for k in read_csv_file:
                print(k)        
            
    
#transform_json_en_csv()