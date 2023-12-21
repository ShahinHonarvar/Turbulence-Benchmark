
import itertools

def return_binary_or_hexa(nums):
    suma = sum(nums)
    if suma % 2 == 0:
        return hex(suma)
    else:
        return bin(suma)
