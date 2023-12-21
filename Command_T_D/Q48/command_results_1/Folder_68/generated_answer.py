
import binary
import hexadecimal

def return_binary_or_hexa(test_tup):
    a, b = test_tup[0], test_tup[9]
    suma = sum(test_tup[1:])
    if suma % 2 == 0:
        return hexadecimal.hexadecimal_str(suma)
    else:
        return binary.binary_str(suma)
