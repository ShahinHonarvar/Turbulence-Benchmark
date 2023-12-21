
def prime_factors(my_list):
    # Get the value at index 37 in the list
    num = my_list[37]
    # Initialize an empty set to store the prime factors

    prime_factors = set()

    # Iterate from 2 to the square root of the number

    for i in range(2, int(num ** 0.5) + 1):
        # If the number is divisible by i, it is not prime

        if num % i == 0:
            break

        # If we reach the end of the loop, the number is prime

        if i > int(num ** 0.5):
            prime_factors.add(num)

    return prime_factors
