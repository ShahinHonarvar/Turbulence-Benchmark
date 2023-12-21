
def find_primes_between_indices(my_list):
    prime_numbers = []
    for i in range(25, 73):
        if my_list[i] > 1:
            for j in range(2, int(my_list[i]**0.5) + 1):
                if my_list[i] % j == 0:
                    break
            else:
                prime_numbers.append(my_list[i])
    return sorted(prime_numbers)
