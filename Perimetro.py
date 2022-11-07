#Programma in python per il calcolo del perimetro di tre figure geometriche

import math   #libreria per piGreco

print ("Il seguente programma calcolca:\n")                 #funzioni di stampa
print ("il perimetro di un quadrato e di un rettangolo,")   #per l'introduzione all'utente
print ("una cinconferenza \n")                              #sullo scopo del programma


x = int (input ("\nDigitare: 1 per Quadrato; 2 per Rettangolo; 3 per Circonferenza: ")) #input per selezionare l'operazione


if (x == 1):  #costrutto if-elif-else per la selezione dell'operazione
        x = int (input ("\nInserisci lato: "))  #input per inserire lato quadrato
        print ("Perimetro Quadrato: ", x*4)     #stampa a video del risultato
elif (x == 2):
          x = int (input ("\nInserisci base: "))     #input per inserire base quadrato
          y = int (input ("Inserisci altezza: "))    #input per inserire altezza quadrato
          print ("Perimetro Rettangolo: ", x*2+y*2)  #stampa a video del risultato
elif (x == 3):
          x = int (input("\nInserisci raggio: "))  #input per inserire raggio circonferenza
          print ("Circonferenza: ", 2*math.pi*x)     #stampa a video circonferenza
else:  #in caso di input diverso da quelli selezionabili
          print ("Digitare SOLO: 1: Quadrato; 2: Rettangolo; 3: Circonferenza")
