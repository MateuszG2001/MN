import csv
from algorithms import *

rows_number = 0
rows_number_2 = 0
control = 0
epsilon = 0.00001

print("Enter the name of the matrix file (file.txt)")
name_file = input()

print("Enter the number of matrix equations (if all enter 0)")
control = int(input())

if control == 0:
    with open(name_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        rows_number = len(list(reader))
else:
    rows_number = control
rows_number_2 = rows_number + 1

tab = [[0] * rows_number_2 for i in range(rows_number)]

with open(name_file, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for i in range(rows_number):
        row = next(reader)
        for j in range(rows_number_2):
            tab[i][j] = float(row[j])

for j in range(rows_number):
    for k in range(rows_number_2):
        print(tab[j][k], "\t", end="")
    print()

elim = gauss_elimination(rows_number, tab, epsilon)
X = [0] * rows_number

if elim:
    print("Gauss elimination succeeded")
    calc = calculate(rows_number, X, tab, epsilon)
    if calc:
        print("Calculation of unknowns completed successfully")
        for l in range(rows_number):
            print(X[l], "\t", end="")
        print()
else:
    print("The calculated values are too close to 0")
    print("Choose another method to solve this system of equations")

