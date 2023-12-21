
import re

def return_binary_or_hexa(test_list):
    suma=0
    for i in range(38,81):
        if i not in test_list:
            suma+=i
            break
    if suma%2==0:
        return hex(suma)[2:]
    else:
        return bin(suma)[2:]
