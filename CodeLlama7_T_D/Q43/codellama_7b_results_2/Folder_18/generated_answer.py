
def find_primes_between_indices(my_list):
    # Find all prime numbers between indices 430 and 805, inclusive
    primes = []
    for i in range(430, 806):
        if is_prime(my_list[i]):
            primes.append(my_list[i])
    return sorted(primes)

def is_prime(n):

    # Check if a number is prime by iterating from 2 to the square root of the number

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
