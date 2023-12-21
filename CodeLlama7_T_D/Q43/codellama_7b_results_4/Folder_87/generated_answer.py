
def find_primes_between_indices(my_list):
    # Define a list to store the prime numbers
    prime_numbers = []

    # Loop through the indices of the input list
    for i in range(11, 42):
        # Check if the current index value is divisible by any other number than itself and 1
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0:
            continue

        # Loop through the remaining indices of the input list
        for j in range(i + 1, len(my_list)):
            # Check if the current index value is divisible by any other number than itself and 1
            if my_list[j] % my_list[i] == 0:
                break

        # If the current index value is prime, add it to the list of prime numbers
        else:
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 11 to index 41, both inclusive
    return sorted(prime_numbers)
