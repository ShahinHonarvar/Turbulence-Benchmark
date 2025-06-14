
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list of integers starting from index 7
    for i in range(7, len(my_list)):
        # Check if the current number is divisible by any number between 2 and the square root of the current number
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0 or my_list[i] % 5 == 0 or my_list[i] % 7 == 0:
            # If it is not divisible by any number between 2 and the square root of the current number, it is prime
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers
