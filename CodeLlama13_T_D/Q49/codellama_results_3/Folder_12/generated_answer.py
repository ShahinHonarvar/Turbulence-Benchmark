
def if_decimal_is_divisible(binary):
    binary = int(binary, 2) # convert from binary to decimal
    fibonacci = [0] + [1] + [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597] # Fibonacci sequence
    for i in range(len(fibonacci)):
        if binary % fibonacci[i] == 0:
            return True
    return False
