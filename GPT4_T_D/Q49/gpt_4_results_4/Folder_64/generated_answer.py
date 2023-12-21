
def if_decimal_is_divisible(bin_str):
    decimal_number = int(bin_str, 2)
    def fib(n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            fib_numbers=[0,1]
            for i in range(2,n+1):
                fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
            return fib_numbers[n]
    tenth_fibonacci = fib(10)
    
    if decimal_number % tenth_fibonacci == 0:
        return True
    else:
        return False
