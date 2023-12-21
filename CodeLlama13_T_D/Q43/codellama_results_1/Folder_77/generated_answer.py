
def find_primes_between_indices(my_list):
    primes = []
    for i in range(287, 928+1):
        if my_list[i] == 0:
            continue
        is_prime = True
        for j in range(2, int(math.sqrt(my_list[i]))+1):
            if my_list[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(my_list[i])
    return sorted(primes)
