import random   

char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
n_char = int(input("Inserisci il numero di caratteri per la tua password:"))

password = ""
for i in range(n_char):
    password = password + char[random.randint(1, len(char))]

print("Questa è la tua nuova password:", password)
import discord