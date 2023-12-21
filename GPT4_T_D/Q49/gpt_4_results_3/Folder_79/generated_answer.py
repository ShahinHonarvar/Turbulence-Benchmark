
def if_decimal_is_divisible(binary_string):
    fibo_seq = [0, 1]
    count = 2
    while count < 13:
        fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
        count += 1
    decimal_num = int(binary_string, 2)
    if decimal_num % fibo_seq[-1] == 0:
        return True
    else:
        return False
