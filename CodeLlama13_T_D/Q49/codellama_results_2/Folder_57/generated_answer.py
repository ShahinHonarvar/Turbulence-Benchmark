
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(80):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return (num % fibonacci[80]) == 0
