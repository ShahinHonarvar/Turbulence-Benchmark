
def if_decimal_is_divisible(bin_string):
    # Generate 84th Fibonacci number
    fib_nums = [0, 1]
    while len(fib_nums) < 84:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    fib_84 = fib_nums[-1]
    
    # Convert binary string to integer
    dec_int = int(bin_string, 2)
    
    # Check if divisible
    return dec_int % fib_84 == 0
