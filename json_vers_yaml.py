def transform_json_en_yaml() :
    import json, yaml
    with open("page0.json") as file:
        page = json.load(file)
#        print(page)
        with open("fic.yaml", "w") as f:
            for i in page:
                yaml.dump(i, f,allow_unicode= True) 
            yaml_file = open("fic.yaml", "r")
            for k in yaml_file:
                print(k)

#transform_json_en_yaml()
    
    