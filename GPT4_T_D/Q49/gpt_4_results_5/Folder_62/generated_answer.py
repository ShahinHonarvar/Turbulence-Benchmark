
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n<0:
            return "Incorrect input"

        elif n==1:
            return 0

        elif n==2:
            return 1

        else:
            a = 0
            b = 1
            for i in range(2,n):
                c = a + b
                a = b
                b = c
            return b

    decimal_number = int(binary_string, 2)
    fibonacci_number = fibonacci(130)
    
    return decimal_number % fibonacci_number == 0
