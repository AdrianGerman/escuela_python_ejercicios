import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as file:
       total = sum(int(r[1]) for r in csv.reader(file))
   return total

response = read_csv('./data.csv')
print(response)
