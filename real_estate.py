import numpy as np

with open("flat_price.csv") as file_name:
    array = np.loadtxt(file_name, delimiter=";")

print(array)
