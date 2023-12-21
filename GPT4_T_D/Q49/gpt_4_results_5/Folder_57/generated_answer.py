
def if_decimal_is_divisible(binary_representation):
    def compute_fibonacci(n):
        fibonacci_numbers = [0, 1]
        while len(fibonacci_numbers) < n:
            fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        return fibonacci_numbers[-1]
    
    decimal_number = int(binary_representation, 2)
    fibonacci_num = compute_fibonacci(81) 

    return decimal_number % fibonacci_num == 0
