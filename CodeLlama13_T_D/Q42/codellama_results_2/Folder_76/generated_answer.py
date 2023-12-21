
def prime_factors(my_list):
    return set([i for i in range(2, my_list[537]) if my_list[537] % i == 0 and is_prime(i)])
