def transform_csv_en_xml():
    from dict2xml import dict2xml
    import csv
    #let's transform our csv file on dictionn
    with open ("donnees.csv", "r") as lok:
        myread = csv.DictReader(lok)
        #now let's transform our dict to xml
        fic_xml = dict2xml(myread)
        print(fic_xml)
#transform_csv_en_xml ()          
       