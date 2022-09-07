def transform_xml_en_yaml() :
    import xmltodict , yaml
    import pprint
    with open('book.xml', 'r') as file:
        my_xml = file.read()
    # Use xmltodict to parse and convert 
# the XML document
        my_dict = xmltodict.parse(my_xml)
        with open("foc.yaml", "w") as f:
            for i in my_dict:
                yaml.dump(i, f,allow_unicode= True) 
        with open("foc.yaml", "r") as yaml_file:
            for k in yaml_file:
                print(k)
transform_xml_en_yaml()    