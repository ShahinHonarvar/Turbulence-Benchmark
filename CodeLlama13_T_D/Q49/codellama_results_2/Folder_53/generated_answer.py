
def if_decimal_is_divisible(binary_repr):
    # Convert binary representation string to int
    decimal = int(binary_repr, 2)
    
    # Find the 64th number that occurs in the Fibonacci sequence
    fib_nums = [0, 1]
    for i in range(2, 65):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    
    # Check if the decimal integer is divisible by the 64th number that occurs in the Fibonacci sequence
    return decimal % fib_nums[-1] == 0
