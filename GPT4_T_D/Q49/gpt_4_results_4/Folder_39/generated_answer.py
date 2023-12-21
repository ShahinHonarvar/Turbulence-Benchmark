
def if_decimal_is_divisible(binary_string):
    fib_array = [0,1]  
    for i in range(2, 15):  
        fib_array.append(fib_array[i-1] + fib_array[i-2])
    decimal = int(binary_string, 2)
    if decimal % fib_array[-1] == 0:
        return True
    else:
        return False
