
def prime_factors(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")
    # Get the integer at index 132
    num = my_list[132]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible by i, it is not prime
        if num % i == 0:
            break
    # If the number is a prime, add it to the set of prime factors
    if num > 1 and all(num % j != 0 for j in range(2, int(num ** 0.5) + 1)):
        prime_factors.add(num)
    return prime_factors
