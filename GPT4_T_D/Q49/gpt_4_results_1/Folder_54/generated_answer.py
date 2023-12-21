
def if_decimal_is_divisible(binary_str):
    fib_cache = [0, 1]
    while len(fib_cache) < 34:
        fib_cache.append(fib_cache[-1] + fib_cache[-2])
    
    decimal = int(binary_str, 2)
    return decimal % fib_cache[33] == 0
