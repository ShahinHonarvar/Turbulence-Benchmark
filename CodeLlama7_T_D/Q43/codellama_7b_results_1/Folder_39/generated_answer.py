
def find_primes_between_indices(my_list):
    # Check if the list is empty or has less than 15 elements
    if len(my_list) < 15:
        return []

    # Initialize an empty list to store the prime numbers

    prime_numbers = []

    # Loop through the list from index 15 to index 81 (both inclusive)

    for i in range(15, 82):

        # Check if the current element is divisible by any number between 2 and the square root of the current element

        for j in range(2, int(i ** 0.5) + 1):

            if i % j == 0:

                break


        # If the current element is not divisible by any number between 2 and the square root of the current element, it is prime

        else:

            prime_numbers.append(i)

    # Sort the list of prime numbers in descending order

    return sorted(prime_numbers, reverse=True)
