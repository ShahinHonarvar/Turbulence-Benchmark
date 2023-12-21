
def prime_factors(my_list):
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Loop through each element in the list
    for i in range(len(my_list)):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is, add it to the set of prime factors
            prime_factors.add(my_list[i])
    return prime_factors

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If n is divisible by i, it is not prime
            if n % i == 0:
                return False

    # If we reach this point, n is prime
    return True
