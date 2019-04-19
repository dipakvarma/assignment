f = open("demo.txt", "w")
f.write("ketul shah")
f = open("demo.txt")
print(f.read())






'''import csv
filename="test.csv"

fields = [ ]
rows = [ ]

with open(filename,'r') as csvfile:
        csvreader=csv.reader(csvfile)
        
        fields = csvreader.next()
        
        rows = csvreader.next()
        
        for row in csvreader: 
                rows.append(row) 
        
        

for row in rows[:4]: 
    # parsing each column of a row 
   
    for col in row: 
        print("%60s"%col), 
    print('\n') '''
    
