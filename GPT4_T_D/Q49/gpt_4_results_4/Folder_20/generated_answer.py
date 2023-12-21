
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_num = int(binary_string, 2)
    hundredth_fibonaci = fibonacci(100)
    
    return decimal_num % hundredth_fibonaci == 0
