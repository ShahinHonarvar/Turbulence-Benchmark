
def if_decimal_is_divisible(binary):
    def fibonacci(n): 
        if n <= 1: 
            return n 
        else: 
            return(fibonacci(n-1) + fibonacci(n-2)) 

    number = int(binary, 2)
    fib_24 = fibonacci(24)
    
    if number % fib_24 == 0:
        return True
    else:
        return False
