
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib_array = [0, 1]
        while len(fib_array) <= n:
            fib_array.append(fib_array[-1] + fib_array[-2])
        return fib_array[n]
    
    decimal_number = int(binary_string, 2)
    fib_num = fibonacci(188)

    return decimal_number % fib_num == 0
