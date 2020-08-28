# Importera libraries.
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

datalist = [] # Tom Lista för data.
datalist2 = [] # En annan tom lista för ett annat dataset.
datalist3 = []
datalist4 = []

# Funktion för att läsa csv fil och appenda i listorna
def readCSVdata():
    with open('Datainsamling/query4_mysql.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            every_other = row[1::2]
            for i in every_other:
                datalist.append(min(float(i) * 1000, 300)) #Gångrar varje värde med 1000 för att få sekunder till millisekunder
    # With open... som tidigare för att importera fler dataset.
    with open('Datainsamling/query4_mongodb.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            every_other = row[1::2]
            for i in every_other:
                datalist2.append(min(float(i) * 1000, 600)) #Gångrar varje värde med 1000 för att få sekunder till millisekunder
    with open('Datainsamling/baseline_mysql_1000.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            every_other = row[1::2]
            for i in every_other:
                datalist3.append(min(float(i) * 1000, 600)) #Gångrar varje värde med 1000 för att få sekunder till millisekunder
    with open('Datainsamling/baseline_mongodb_1000.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            every_other = row[1::2]
            for i in every_other:
                datalist4.append(min(float(i) * 1000, 600)) #Gångrar varje värde med 1000 för att få sekunder till millisekunder
# Funktion för att rendera ut plots.
def render():
    fig, (ax) = plt.subplots(1) #Skapa en subplot för en figur
    # Går att repetera för att skapa fler diagram
    fig, (ax2) = plt.subplots(1)

    ax.set_title('Query 4')
    ax.set_xlabel('Number of searches')
    ax.set_ylabel('Loading times (ms)')

    ax2.set_title('Query 4')
    ax2.set_xlabel('Mean and standard deviation')
    ax2.set_ylabel('Loading times (ms)')

    #Rita ut linjediagram
    ax.plot(datalist, color="blue", alpha = 1, label = "MySQL (Query 1)")
    ax.plot(datalist2, color="red", alpha= 1, label = "MongoDB (Query 1)")
    ax.plot(datalist3, color="blue", alpha= 0.45, label = "MySQL (Baseline)")
    ax.plot(datalist4, color="red", alpha= 0.45, label = "Mongodb (Baseline)")
    #Går att repetera för fler linjer i samma figur.

    #Göra dataLists till arrays
    array1= np.array(datalist)
    type(array1)
    array2= np.array(datalist2)
    type(array2)
    array3= np.array(datalist3)
    type(array3)
    array4= np.array(datalist4)
    type(array4)

    #Standardavikelse
    sd1 = np.std(array1)
    #print("Standard Deviation : ", sd1)
    sd2 = np.std(array2)
    #print("Standard Deviation : ", sd2)
    sd3 = np.std(array3)
    #print("Standard Deviation : ", sd3)
    sd4 = np.std(array4)
    #print("Standard Deviation : ", sd4)

    #Median på stapeldiagrammen
    mean1 = np.mean(array1)
    mean2 = np.mean(array2)
    mean3 = np.mean(array3)
    mean4 = np.mean(array4)

    #Skapa stapeldiagram
    ax2.bar(0, mean1, color="blue", label = "MySQL (Query 1)", width= 0.5, align='center', alpha= 0.8, yerr= sd1, capsize=10)
    ax2.bar(1, mean2, color="red", label = "MongoDB (Query 1)", width= 0.5, align='center', alpha= 0.8, yerr=sd2, capsize=10)
    ax2.bar(2, mean3, color="blue", label = "MySQL (Baseline)", width= 0.5, align='center', alpha= 0.5, yerr=sd3, capsize=10)
    ax2.bar(3, mean4, color="red", label = "Mongodb (Baseline)", width= 0.5, align='center', alpha= 0.5, yerr=sd4, capsize=10)
    #Går även att repetera

    #För att ta bort axel:
    ax2.axes.get_xaxis().set_ticks([])

    #Skapa "legend"
    ax.legend()
    ax2.legend()
    #ax3.legend()
    #ax4.legend()

    #Sätta limit på höjden
    ax.set(ylim=(-0,300))
    ax2.set(ylim=(0,200))
    #ax3.set(ylim=(0,300))
    #ax4.set(ylim=(0,200))

    #Visa graferna
    plt.show()

#Läs datan
readCSVdata()

#Rendera datan
render()
