def  transform_xml_en_csv():
    import xmltodict 
    import pprint
    with open('book.xml', 'r') as file:
        my_xml = file.read()
    # Use xmltodict to parse and convert 
# the XML document
    my_dict = xmltodict.parse(my_xml)
  
# Print the dictionary
#    pprint.pprint(my_dict, indent=1)
#converting my dict to csv
    with open ("dox.csv", "w") as csv_file:
        for key in my_dict.keys():
                csv_file.write("%s, %s\n" % (key, my_dict[key])) 
    with open("dox.csv", "r") as read_csv_file:
        for k in read_csv_file:
            print(k)        

#transform_xml_en_csv()      
     