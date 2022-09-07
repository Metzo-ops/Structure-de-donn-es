def transform_csv_en_json() :
    # d'abord,transformation du fichier csv en dictionnaire
    import csv,json
    with open("donnees.csv","r") as ficc: 
        pagediccsv = csv.DictReader(ficc) 
    #transformation du dictionnaire en fichier json
        for i in pagediccsv:
            jsonficc = json.dumps(i, indent=3)
            print(jsonficc)
#transform_csv_en_json()        
