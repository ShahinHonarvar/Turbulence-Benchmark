
def find_primes_between_indices(my_list):
    # Create a new list to store the prime numbers
    prime_numbers = []

    # Iterate through the list of integers, starting from index 38
    for i in range(38, len(my_list)):
        # Check if the current number is divisible by any other number in the range (38 to 54)
        for j in range(38, i+1):
            if my_list[i] % my_list[j] == 0:
                break

        else:

            # If the current number is not divisible by any other number in the range (38 to 54), then it is a prime number
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 38 to index 54, both inclusive
    return sorted(prime_numbers, reverse=True)
