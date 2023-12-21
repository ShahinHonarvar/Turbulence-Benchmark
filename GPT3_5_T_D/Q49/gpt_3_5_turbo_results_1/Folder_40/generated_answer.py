
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(bin_str, 2)
    fourth_fibonacci = fibonacci(3)
    return decimal % fourth_fibonacci == 0
