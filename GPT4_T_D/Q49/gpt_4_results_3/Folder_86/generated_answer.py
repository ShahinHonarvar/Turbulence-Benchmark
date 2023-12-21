
def if_decimal_is_divisible(binary_str):
    fibo_seq = [0, 1]
    while len(fibo_seq) < 135:
        fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
    integ = int(binary_str, 2)
    if integ % fibo_seq[134] == 0:
        return True
    else:
        return False
