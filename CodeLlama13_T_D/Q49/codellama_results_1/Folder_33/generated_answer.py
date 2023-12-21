
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    decimal = int(binary_representation, 2)
    return (decimal % fibonacci[13]) == 0
