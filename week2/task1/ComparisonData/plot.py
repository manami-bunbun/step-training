import csv
import numpy as np
import matplotlib.pyplot as plt


def read_data_from_csv(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
    return np.array(x), np.array(y)

# 近似線
def calculate_approximation(x, y):
    coefficients = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coefficients)
    return polynomial


def plot_data_with_approximation(x, y, polynomial, name, color):
    plt.scatter(x, y, color=color, label=name)
    plt.plot(x, polynomial(x), color=color)
    plt.xlabel('iteration')
    plt.ylabel('time')
    plt.title('Comparison of the performance of the hash table')
    plt.legend()

if __name__ == "__main__":

    filename1 = 'initial_hash_table.csv'
    filename2 = 'initial-hash_table.csv'
    x1, y1 = read_data_from_csv(filename1)
    x2, y2 = read_data_from_csv(filename2)


    polynomial1 = calculate_approximation(x1, y1)
    polynomial2 = calculate_approximation(x2, y2)


    plot_data_with_approximation(x1, y1, polynomial1, 'initial_hash_table.py(sample code)', 'red')
    plot_data_with_approximation(x2, y2, polynomial2,'improved_hash_table.py(with Rehashing/new hash calculation)', 'blue')


    plt.show()
