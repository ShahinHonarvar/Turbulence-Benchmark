
def if_decimal_is_divisible(binary_representation):
    fib = [0,1]
    for i in range(2,68):
        fib.append(fib[i-1] + fib[i-2])
    decimal_number = int(binary_representation, 2)
    if decimal_number % fib[67] == 0:
        return True
    else:
        return False
