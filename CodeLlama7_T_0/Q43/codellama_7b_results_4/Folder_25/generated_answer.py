
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(52, 54):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    break

            else:

                prime_numbers.append(my_list[i])

    return sorted(prime_numbers)
