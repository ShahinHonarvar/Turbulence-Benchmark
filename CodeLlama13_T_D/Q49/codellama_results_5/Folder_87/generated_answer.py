
def if_decimal_is_divisible(binary_str):
    # Convert the binary string to a list of digits
    digits = [int(d) for d in binary_str]
    
    # Calculate the decimal value of the number represented by the digits
    decimal = sum([digit * 2**i for i, digit in enumerate(digits[::-1])])
    
    # Check if the decimal value is divisible by the 180th Fibonacci number
    fib_nums = [0, 1] + [fib_nums[-1] + fib_nums[-2] for _ in range(len(digits) - 2)]
    return decimal % fib_nums[179] == 0
