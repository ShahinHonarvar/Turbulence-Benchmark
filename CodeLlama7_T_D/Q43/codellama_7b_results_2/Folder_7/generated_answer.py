
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list starting from index 239
    for i in range(239, len(my_list)):
        # Check if the current element is divisible by any of the elements before it
        for j in range(i-1, -1, -1):
            if my_list[i] % my_list[j] == 0:
                break

        # If the current element is not divisible by any of the elements before it, then it is prime
        else:
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    return prime_numbers
