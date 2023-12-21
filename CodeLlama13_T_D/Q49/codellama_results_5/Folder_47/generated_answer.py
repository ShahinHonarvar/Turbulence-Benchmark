
def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fibonacci = [0, 1]
    for i in range(n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i])
    return n % fibonacci[93] == 0
