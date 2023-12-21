
def prime_factors(my_list):
    # Find the largest prime factor of the number at index 126
    max_prime = 0
    for i in range(1, my_list[126] + 1):
        if my_list[126] % i == 0 and is_prime(i):
            max_prime = i

# Check if a number is prime using the Sieve of Eratosthenes algorithm
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
