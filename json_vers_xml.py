def transform_json_en_xml() :
    from dict2xml import dict2xml
    import json
    with open("page0.json") as file:
        page = json.load(file)
#        print(page)
        dict_to_xml = dict2xml(page)
        print(dict_to_xml)

#transform_json_en_xml()        
    