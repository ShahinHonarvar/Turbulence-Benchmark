
def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, 78):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])
    if decimal % fibonacci_seq[-1] == 0:
        return True
    else:
        return False
