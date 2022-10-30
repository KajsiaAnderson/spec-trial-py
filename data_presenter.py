# Open the CupcakeInvoices.csv.
data = open('./CupcakeInvoices.csv')

# problem 1
# Loop through all the data and print each row.

for row in data:
    print(row)

# problem 2
# Loop through all the data and print the type of cupcakes purchased.

for row in data:
  values = row.split(',')
  print(values[2])

# problem 3
# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

for row in data:
    values = row.split(',')
    total = int(values[3]) * float(values[4])
    print(total)

# problem 4
# Loop through all the data, and print out the total for all invoices combined.
total = 0
for row in data:
    values = row.split(',')
    total = total + (int(values[3]) * float(values[4]))
print(total)

# problem 5
# Close your open file.
data.close()