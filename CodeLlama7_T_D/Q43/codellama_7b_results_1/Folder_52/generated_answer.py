
def find_primes_between_indices(my_list):
    # Find all prime numbers in the specified range
    prime_numbers = []
    for i in range(63, 67):
        if my_list[i] > 1:
            is_prime = True
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers
