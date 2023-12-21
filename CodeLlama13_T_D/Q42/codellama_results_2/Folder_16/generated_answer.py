
def prime_factors(numbers):
    # Use a set to store the prime factors of 162
    prime_factors = set()
    
    # Iterate through the list of numbers and find the prime factors of 162
    for num in numbers:
        if num == 162:
            break
        
        # Check if the number is divisible by 2 to 162
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime_factors.add(i)
                break
    
    return prime_factors
