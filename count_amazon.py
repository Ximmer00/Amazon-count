import csv
from collections import defaultdict

columns = defaultdict(list)
amazon_extract = 'Dsar_command_history.csv' #The location of csv file extracted from amazon

with open(amazon_extract) as file:
        reader = csv.DictReader(file, delimiter=';')
        print(reader.fieldnames)
        for row in reader:
                for (k,v) in row.items():
                        columns[k].append(v)

total = 0
tot_taxes = 0

for prix in (columns['Prix']):
        prix_correct = prix.strip().replace(',', '.')
        total += float(prix_correct)
print("You spent with Amazon", round(total,2), '€ (Without taxes)')

for prix in (columns['Taxe']):
        prix_correct = prix.strip().replace(',', '.')
        tot_taxes += float(prix_correct)
        
print("You spent in total to Amazon", round(total+tot_taxes,2), '€ (Taxes included)')
print("Value of VAT:", round(tot_taxes,2), "€")

