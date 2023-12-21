
def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    fibonacci = [0, 1]
    for i in range(2, n+1):
        fibonacci.append((fibonacci[i-1] + fibonacci[i-2]) % (10**9 + 7))
    return n % fibonacci[174] == 0
