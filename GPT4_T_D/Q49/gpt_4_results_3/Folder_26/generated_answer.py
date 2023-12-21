
def if_decimal_is_divisible(bin_string):
    fibs = [0, 1]
    for i in range(136):
        fibs.append(fibs[-1] + fibs[-2])
    decimal = int(bin_string, 2)
    return decimal % fibs[-1] == 0
