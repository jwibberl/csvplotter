#from https://github.com/Generation-UK-I/DE-NAT4-TECH-CONTENT/blob/main/data-encoding/handouts/data-encoding-cheatsheet.md
#slightly modified for investigation

import csv

# open people.csv and write row
with open('people.csv', mode='w') as file:
  writer = csv.writer(file, delimiter=',')
  # instruct the write to write a row
  writer.writerow(['first_name', 'last_name', 'age'])
  writer.writerow(['Joe', 'Bloggs', 40])
  writer.writerow(['Jane', 'Smith', 50])

# open the people.csv and write row from dict
with open('people.csv', mode='w') as file:
  # set the headers for the CSV
  fieldnames = ['first_name', 'last_name', 'age']
  writer = csv.DictWriter(file, fieldnames=fieldnames)
  # instruct the writer to know to write the headers
  writer.writeheader()
  # instruct the writer to write the row
  writer.writerow({
    'first_name': 'Jan',
    'last_name': 'Smith',
    'age': 60
  })