import re
 Fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
def if_decimal_is_divisible(binary):
    return (10**len(binary)-1-int(binary,2))%178==Fibonacci[len(binary)-1]
