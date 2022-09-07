def transform_yaml_en_csv() :
    import yaml
    # convertissons notre fichier yaml en dictionnaire
    with open ("yaml_file.yaml","r" ) as yamfil:
        kinp  = yaml.load(yamfil)
 #           print(i)
    #maintenant,convertissons notre  dictionnaire en csv 
    with open ("kox.csv", "w") as csv_file:
        for i in kinp:
            for key in i.keys():
                csv_file.write("%s, %s\n" % (key, i[key]))
    with open("kox.csv", "r") as read_csv_file:
        for k in read_csv_file:
                print(k)        

#transform_yaml_en_csv()        