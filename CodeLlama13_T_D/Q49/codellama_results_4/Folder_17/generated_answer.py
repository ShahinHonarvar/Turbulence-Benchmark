
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, num + 1):
        fibonacci_seq.append((fibonacci_seq[i - 1] + fibonacci_seq[i - 2]) % 10)
    return fibonacci_seq[154] == 0
