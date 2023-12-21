
def if_decimal_is_divisible(binary_string):
    fibo_list = [0, 1]
    for i in range(2, 46):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    decimal_integer = int(binary_string, 2)
    if decimal_integer % fibo_list[-1] == 0:
        return True
    else:
        return False
