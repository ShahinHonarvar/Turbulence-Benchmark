
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        arr = [0, 1]
        while len(arr) < n:
            arr.append(arr[-1] + arr[-2])
        return arr[n-1]

    binary_decimal = int(binary_string, 2)
    fibonacci_69th = fibonacci(69)

    if binary_decimal % fibonacci_69th == 0:
        return True
    else:
        return False
