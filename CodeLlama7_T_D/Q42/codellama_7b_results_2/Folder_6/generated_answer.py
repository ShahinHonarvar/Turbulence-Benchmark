
def prime_factors(my_list):
    # Find the integer at index 790
    target = my_list[790]
    # Initialize an empty set to store the prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the target integer
    for i in range(2, int(target ** 0.5) + 1):
        # If the current number is a factor of the target integer, add it to the set of prime factors
        if target % i == 0:
            prime_factors.add(i)
    return prime_factors
