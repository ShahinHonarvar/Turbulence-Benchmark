
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list and check if each element is a prime number
    for i in range(84, 97 + 1):
        if my_list[i] == 0:
            continue

        else:

            for j in range(2, int(my_list[i]) ** 0.5 + 1):
                if my_list[i] % j == 0:
                    break

            else:

                prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers in the specified range, or an empty list if no prime number exists in that range
    return sorted(prime_numbers)
