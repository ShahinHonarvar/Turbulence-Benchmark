
import sys

def return_binary_or_hexa(tup):
    a, b = tup[3], tup[8]
    suma = sum(i for i in range(a+1, b-1) if i not in tup[3:8])
    if suma % 2 == 1:
        return bin(suma).zfill(len(bin(suma)))
    else:
        return hex(suma).zfill(len(hex(suma)))
