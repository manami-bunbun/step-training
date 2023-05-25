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


def plot_data_with_approximation(x, y, name, color):
    # change as you like
    plt.plot(x, y, color=color, label=name)
    # plt.scatter(x, y, color=color, label=name)
    # plt.plot(x, polynomial(x), color=color)
    plt.xlabel('iteration')
    plt.ylabel('time')
    plt.title('Comparison of the hash function')
    plt.legend()
    
def drawGraphfromCSV(filename, name, color):
    x, y = read_data_from_csv(filename)
    # polynomial = calculate_approximation(x, y)
    plot_data_with_approximation(x, y, name, color)

if __name__ == "__main__":

    #change
    fileList = ['3timesHash.csv',
                '17timesHash.csv',
                '29timesHash.csv',
                '43timesHash.csv',
                '97timesHash.csv',
                '499timesHash.csv']
  
    color = ['red', 'blue', 'green', 'yellow', 'black', 'pink']
    i=0
    
    # change 
    dir = '/Users/manami/22:23/step2023/step-training/week2/task1/ComparisonData/'
    
    for file in fileList:
        drawGraphfromCSV(dir+file, file, color[i])
        i+=1

    plt.show()
