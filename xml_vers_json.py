def transform_xml_en_json() :
    import json
    import xmltodict 
    import pprint
    with open('book.xml', 'r') as file:
        my_xml = file.read()
    # Use xmltodict to parse and convert 
# the XML document
        my_dict = xmltodict.parse(my_xml)
        json_data = json.dumps(my_dict)
        with open("data.json", "w") as json_file:
            json_file.write(json_data)
            json_file.close() 
        with open("data.json", "r") as jso:
            for k in jso:
                print(k)
#transform_xml_en_json()                
    