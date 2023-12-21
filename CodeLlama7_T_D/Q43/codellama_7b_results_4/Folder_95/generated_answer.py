
def find_primes_between_indices(my_list):
    # Find all prime numbers between indices 19 and 71, inclusive
    prime_numbers = []
    for i in range(19, 72):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    break
            else:
                prime_numbers.append(my_list[i])
    return sorted(prime_numbers)
