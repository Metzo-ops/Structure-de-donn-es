import csv
import moncsv
import monjson
import monyaml
import csv_vers_json
import csv_vers_yaml
import csv_vers_xml
import json_vers_xml
import json_vers_yaml
import json_vers_csv
import yaml_vers_csv
import yaml_vers_json
import yaml_vers_xml
import xml_vers_csv
import xml_vers_json
import xml_vers_yaml
import monxml
formatI = input("choisis un format de fichier,en lettre miniscule\n")
if formatI == "csv" :
    moncsv.mycsv()
    formatF = input("choisissez un format  auquel vous voulez mettre le fichier\n") 
    if formatF == "json" :
        csv_vers_json.transform_csv_en_json()
    elif formatI == "yaml" :
        csv_vers_yaml.transform_csv_en_yaml()
    elif formatF == "xml" :
        csv_vers_xml.transform_csv_en_xml()
    else:
        print("le format auquel vous voulez mettre votre fichier csv n'est pas pris en charge\n")        
elif formatI == "json" :             
    monjson.myjson()
    formatF = input("choisissez un format  auquel vous voulez mettre le fichier,en miniscule\n") 
    if formatF == "csv" :
        json_vers_csv.transform_json_en_csv()
    elif formatF == "yaml" :
        json_vers_yaml.transform_json_en_yaml()
    elif formatF == "xml" :
        json_vers_xml.transform_json_en_xml()        
    else:
        print("le format auquel vous voulez mettre votre fichier json n'est pas pris en charge\n")
elif formatI == "yaml" :
    monyaml.foncyaml()
    formatF = input("choisissez un format  auquel vous voulez mettre le fichier\n") 
    if formatF == "csv" :
        yaml_vers_csv.transform_yaml_en_csv()
    elif formatF == "json" :
        yaml_vers_json.transform_yaml_en_json()
    elif formatF == "xml" :
        yaml_vers_xml.transform_yaml_en_xml()
    else :
          print("le format auquel vous voulez mettre votre fichier yaml n'est pas pris en charge\n")          
elif formatI == "xml" :
    monxml.foncxml()
    formatF = input("saisissez le format auquel vous voulez transformer le fichier xml\n")
    if formatF == "csv" :
         xml_vers_csv.transform_xml_en_csv()
    elif formatF == "json" :
        xml_vers_json.transform_xml_en_json()
    elif formatF == "yaml" :
        xml_vers_yaml.transform_xml_en_yaml()    
    else :
      print("le format auquel vous voulez mettre votre fichier xml n'est pas pris en charge\n")  
else :
    print("format non prix en charge")
