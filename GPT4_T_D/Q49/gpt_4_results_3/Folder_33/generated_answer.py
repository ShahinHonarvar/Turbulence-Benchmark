
def if_decimal_is_divisible(binary_string):
    fibo_index = 134
    fibo_list = [0, 1]

    for i in range(2, fibo_index+1):
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])

    decimal = int(binary_string, 2)
    return decimal % fibo_list[fibo_index] == 0
