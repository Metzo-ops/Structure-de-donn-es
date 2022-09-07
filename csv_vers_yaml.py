from curses import meta
from pickle import TRUE
from re import T


def transform_csv_en_yaml():
    # d'abord,transformation du fichier csv en dictionnaire
    import csv,yaml
    vid = []
    with  open("donnees.csv","r")as file: 
        pagediccsv = csv.DictReader(file)
        with open("meta.yaml", "w") as f:
            for i in pagediccsv:
                yaml.dump(i, f,allow_unicode= True) 
            yaml_file = open("meta.yaml", "r")
            for k in yaml_file:
                print(k)
                                 
#transform_csv_en_yaml()           