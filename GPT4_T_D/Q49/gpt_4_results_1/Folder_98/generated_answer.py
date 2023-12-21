
def if_decimal_is_divisible(binary_rep):
    fibonacci = [0, 1]
    for i in range(2, 14):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    int_num = int(binary_rep, 2)
    if int_num % fibonacci[13] == 0:
        return True
    else:
        return False
