
def prime_factors(my_list):
    # Find the number at index 35 in the list
    num = my_list[35]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all the divisors of the number
    for i in range(1, num + 1):
        if num % i == 0:
            # If the divisor is prime, add it to the set of prime factors
            if is_prime(i):
                prime_factors.add(i)
    return prime_factors

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all the numbers from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If n is divisible by any number between 2 and the square root of n, it is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is divisible only by 1 and itself, it is prime
    return True
