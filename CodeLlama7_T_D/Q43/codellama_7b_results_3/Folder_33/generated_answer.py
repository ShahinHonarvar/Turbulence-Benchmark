
def find_primes_between_indices(my_list):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 289 to index 381, both inclusive
    for i in range(289, 382):

        # Check if the number is divisible by any of the previous prime numbers

        for j in range(i-1, -1, -1):

            if my_list[i] % my_list[j] == 0:
                break

            # If the number is not divisible by any of the previous prime numbers, it is a prime number

            else:

                prime_numbers.append(my_list[i])

                break


    # Return the sorted list of all prime numbers from index 289 to index 381, both inclusive, in descending order

    return sorted(prime_numbers, reverse=True)
