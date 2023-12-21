
def if_decimal_is_divisible(binary_num_str):
    fib_seq = [0, 1]
    num_in_decimal = int(binary_num_str, 2)
    for _ in range(2, 20): 
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return num_in_decimal % fib_seq[-1] == 0
