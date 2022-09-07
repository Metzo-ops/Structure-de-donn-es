def transform_yaml_en_json() :
    import yaml
    import json
     # convertissons notre fichier yaml en dictionnaire
    with open ("yaml_file.yaml","r" ) as yamfil:
        kinp  = yaml.load(yamfil)
        print(kinp)
     #convertissons notre dict en json
        for i in kinp:
            jsonficc = json.dumps(i, indent=3)
            print(jsonficc)

#transform_yaml_en_json()     
