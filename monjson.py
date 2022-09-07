def myjson():
   import json
# je veux ouvrir ma page json comme dictionaire
   with open("page0.json") as file:
        page = json.load(file)
        print(page)        

#myjson()
     
