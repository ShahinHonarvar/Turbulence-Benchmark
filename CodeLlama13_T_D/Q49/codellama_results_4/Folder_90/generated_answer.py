
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, num+1):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    return (num % fibonacci[177] == 0)
