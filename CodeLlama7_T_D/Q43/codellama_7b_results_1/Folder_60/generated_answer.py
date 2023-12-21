
def find_primes_between_indices(my_list):
    # Find all prime numbers between indices 48 and 55, both inclusive
    prime_numbers = []
    for i in range(48, 56):
        if my_list[i] > 1:
            is_prime = True
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    is_prime = False
                    break

            if is_prime:
                prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order

    return sorted(prime_numbers, reverse=True)
