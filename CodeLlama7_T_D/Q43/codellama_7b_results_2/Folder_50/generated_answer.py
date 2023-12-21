
def find_primes_between_indices(my_list):
    # Initialize variables
    prime_numbers = []
    for i in range(23, len(my_list)):
        # Check if the number is divisible by any number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break

        else:

            # If the number is not divisible by any number between 2 and the square root of the number, it is prime

            prime_numbers.append(i)

    return sorted(prime_numbers, reverse=True)
