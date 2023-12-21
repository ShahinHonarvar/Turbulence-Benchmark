
def if_decimal_is_divisible(binary_rep):
    fibo = [0, 1]
    while len(fibo) < 187:
        fibo.append(fibo[-1] + fibo[-2])
    decimal = int(binary_rep, 2)
    return decimal % fibo[186] == 0
