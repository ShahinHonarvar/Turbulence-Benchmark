
def find_primes_between_indices(my_list):
    primes = []
    for i in range(46, 61):
        if my_list[i] in primes: continue
        is_prime = True
        for j in range(2, int(math.sqrt(my_list[i])) + 1):
            if my_list[i] % j == 0:
                is_prime = False
                break
        if is_prime: primes.append(my_list[i])
    return sorted(primes)
