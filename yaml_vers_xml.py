def transform_yaml_en_xml() :
    import yaml
    from dict2xml import dict2xml
    with open ("yaml_file.yaml","r" ) as yamfil:
        kinp  = yaml.load(yamfil)
#        print(kinp)
        for i in kinp:
            dict_to_xml = dict2xml(i)
            print(dict_to_xml)
#transform_yaml_en_xml()        
    