
def prime_factors(my_list):
    # Find the number at index 20 in the list
    num = my_list[20]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through all numbers less than or equal to the number at index 20
    for i in range(2, num + 1):
        # If the number is divisible by i and i is prime...
        if num % i == 0 and is_prime(i):
            # ...add it to the set of prime factors
            prime_factors.add(i)
    return prime_factors

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers less than n
        for i in range(2, n):
            # If n is divisible by i...
            if n % i == 0:
                # ...return False (n is not prime)
                return False

    # If n is greater than 1 and it is not divisible by any number in the range 2 to n-1, it is prime
    return True
