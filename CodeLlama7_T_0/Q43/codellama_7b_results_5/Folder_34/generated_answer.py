
def find_primes_between_indices(my_list):
    # Find the prime numbers in the specified range
    prime_numbers = []
    for i in range(56, 58):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    break

            else:

                prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers
