
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list from index 8 to index 9
    for i in range(8, 10):
        # Check if the current number is divisible by any of the prime factors of its square root
        for prime in get_prime_factors(my_list[i] ** 0.5):
            if my_list[i] % prime == 0:
                # If it is, add it to the set of composite numbers
                composite_nums.add(my_list[i])

    return composite_nums

def get_prime_factors(n):
    # Initialize an empty list to store the prime factors
    prime_factors = []

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # If it is, add it to the list of prime factors
            prime_factors.append(i)

    return prime_factors
