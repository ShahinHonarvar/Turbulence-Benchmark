
def prime_factors(my_list):
    # Get the value at index 478
    num = my_list[478]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        # If i is a factor of num, add it to the set of prime factors
        if num % i == 0:
            prime_factors.add(i)
            # Update num by dividing it by its prime factor
            num = num // i

    # Add the remaining prime factor to the set
    if num > 1:
        prime_factors.add(num)

    return prime_factors
