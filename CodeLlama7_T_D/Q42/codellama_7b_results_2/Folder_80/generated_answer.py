
def prime_factors(my_list):
    # Get the number at index 746
    num = my_list[746]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible by i, it is not prime
        if num % i == 0:
            break

    # If we have reached the end of the loop, the number is prime
    else:
        prime_factors.add(num)

    return prime_factors
