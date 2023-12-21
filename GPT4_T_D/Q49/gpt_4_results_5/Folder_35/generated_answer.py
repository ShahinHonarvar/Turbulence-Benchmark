
def if_decimal_is_divisible(bin_str):
    fib_sequence = [0, 1]
    for i in range(2, 187):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        
    decimal_num = int(bin_str, 2)
    return decimal_num % fib_sequence[186] == 0
