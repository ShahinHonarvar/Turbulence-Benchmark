
def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib_array = [0, 1]
    while len(fib_array) <= 117:
         fib_array.append(fib_array[-1] + fib_array[-2])
    return decimal_number % fib_array[117] == 0
