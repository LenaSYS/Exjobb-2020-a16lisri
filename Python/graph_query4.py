# Importera libraries.
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats

dataList = [] # Tom Lista för data.
dataList2 = [] # En annan tom lista för ett annat dataset.
#dataList3 = []

# Funktion för att läsa csv fil och appenda i listorna
def readCSVdata():
    with open('Datainsamling/query4_mysql.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            every_other = row[1::2]
            for i in every_other:
                dataList.append(min(float(i) * 1000, 300)) #Gångrar varje värde med 1000 för att få sekunder till millisekunder
    # With open... som tidigare för att importera fler dataset.
    with open('Datainsamling/query4_mongodb.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            every_other = row[1::2]
            for i in every_other:
                dataList2.append(min(float(i) * 1000, 600)) #Gångrar varje värde med 1000 för att få sekunder till millisekunder
    #with open('apache2_baseline.csv') as rawdata:
        #readCSV = csv.reader(rawdata, delimiter=",")
        #for rad in readCSV:
            #for i in range(0, len(rad)):
                #if(i % 2):
                    #dataList3.append(int(rad[i]))
# Funktion för att rendera ut plots.
def render():
    fig, (ax) = plt.subplots(1) #Skapa en subplot för en figur
    # Går att repetera för att skapa fler diagram
    fig, (ax2) = plt.subplots(1)

    ax.set_title('Loading times per search')
    ax.set_xlabel('Number of searches')
    ax.set_ylabel('Loading times (ms)')

    ax2.set_title('Median and standard deviation ')
    ax2.set_xlabel('Median')
    ax2.set_ylabel('Loading times (ms)')

    #Rita ut linjediagram
    ax.plot(dataList, color="blue", alpha = 1, label = "MySQL")
    ax.plot(dataList2, color="green", alpha= 1, label = "MongoDB")
    #ax.plot(dataList3, color="red", alpha= 0.8, label = "Baseline (Caching Apache2)")
    #Går att repetera för fler linjer i samma figur.

    #Göra dataLists till arrays
    array1= np.array(dataList)
    type(array1)
    array2= np.array(dataList2)
    #type(array2)
    #array3= np.array(dataList3)
    #type(array3)

    #Standardavikelse
    sd1 = np.std(array1)
    #print("Standard Deviation : ", sd1)
    sd2 = np.std(array2)
    #print("Standard Deviation : ", sd2)
    #sd3 = np.std(array3)
    #print("Standard Deviation : ", sd3)

    #Median på stapeldiagrammen
    median1 = np.median(array1)
    median2 = np.median(array2)
    #median3 = np.median(array3)

    #Skapa stapeldiagram
    ax2.bar(0, median1, color="blue", label = "MySQL", width= 0.5, align='center', alpha= 0.6, yerr= sd1, capsize=10)
    ax2.bar(1, median2, color="green", label = "MongoDB", width= 0.5, align='center', alpha= 0.6, yerr=sd2, capsize=10)
    #ax2.bar(2, median3, color="red", label = "Median Baseline (Caching Apache2)", width= 0.5, align='center', alpha= 0.6, yerr=sd3, capsize=10)
    #Går även att repetera

    #För att ta bort axel:
    ax2.axes.get_xaxis().set_ticks([])

    #Skapa "legend"
    ax.legend()
    ax2.legend()

    #Sätta limit på höjden
    ax.set(ylim=(0,300))
    ax2.set(ylim=(0,200))

    #Visa graferna
    plt.show()

#Läs datan
readCSVdata()

#Rendera datan
render()
