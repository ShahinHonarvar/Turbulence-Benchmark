
import re
def return_binary_or_hexa(tup):
    a, b = sorted(tup)[35], sorted(tup)[64]
    if a + 1 <= b - 1:
        suma = a + 1
        sumb = b - 1
        while suma <= sumb:
            if suma not in tup and sumb not in tup:
                break
            suma += 1
            sumb -= 1
        else:
            return ''
        return (str(suma) + 'b' + str(suma + 1) + '0') if suma % 2 == 1 else (str(suma) + 'x' + str(suma + 1))
