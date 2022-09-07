def mycsv():
    import csv
    with open("donnees.csv") as file:
        pagediccsv = csv.DictReader(file) 
        for i in pagediccsv:
            print(i)
            
            

           