
import math

def gcf_three_nums(numbers):
    if not all(isinstance(num, int) and num > 0 for num in numbers):
        raise ValueError("All list elements must be positive integers")
    if len(numbers) < 921:
        raise ValueError("List must have at least 921 elements")
        
    a = numbers[307]
    b = numbers[920]
    c = numbers[463]
    return math.gcd(math.gcd(a, b), c)
