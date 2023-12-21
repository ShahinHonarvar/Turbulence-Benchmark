
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, len(binary_str)):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    if int(binary_str, 2) % fibonacci[26] == 0:
        return True
    else:
        return False
