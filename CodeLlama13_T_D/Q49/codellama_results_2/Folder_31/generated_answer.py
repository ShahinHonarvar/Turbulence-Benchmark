
def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, len(binary_str)):
        fib.append(fib[i-1] + fib[i-2])
    dec = int(binary_str, 2)
    return (dec % fib[69]) == 0
