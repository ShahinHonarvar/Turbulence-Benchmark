
def prime_factors(my_list):
    # Find the integer at index 29
    num = my_list[29]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible by i, it is not prime
        if num % i == 0:
            break

    # If we have reached the end of the loop, then i is a prime factor
    if i * i > num:
        prime_factors.add(i)

    return prime_factors
