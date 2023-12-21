
def if_decimal_is_divisible(binary_representation):
    fibonacci_nums = [0, 1]
    for i in range(2, 60):
        fibonacci_nums.append(fibonacci_nums[i-1] + fibonacci_nums[i-2])
    sixtyith_fibonacci = fibonacci_nums[-1]
    
    decimal_number = int(binary_representation, 2)
    
    return decimal_number % sixtyith_fibonacci == 0
