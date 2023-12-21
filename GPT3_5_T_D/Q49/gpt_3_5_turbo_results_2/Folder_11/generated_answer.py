
def if_decimal_is_divisible(bin_str):
    fibonacci = [0, 1]
    while fibonacci[-1] < int(bin_str, 2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[15] == int(bin_str, 2):
        return True
    else:
        return False
