
def return_binary_or_hexa(test_list):
    suma = 0
    suma_num = 13
    suma_end = 76
    suma_cnt = 0
    suma_str = 0
    for x in range(suma_num + 1, suma_end):
        if x not in test_list:
            suma += x
            suma_cnt += 1
    if suma_cnt % 2 == 0:
        return hex(suma)
    else:
        return bin(suma)
