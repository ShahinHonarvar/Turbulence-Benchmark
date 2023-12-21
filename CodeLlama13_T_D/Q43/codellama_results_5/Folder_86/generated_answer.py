
def find_primes_between_indices(my_list):
    primes = []
    for i in range(459, 781):
        if my_list[i].is_prime():
            primes.append(my_list[i])
    return sorted(primes)
