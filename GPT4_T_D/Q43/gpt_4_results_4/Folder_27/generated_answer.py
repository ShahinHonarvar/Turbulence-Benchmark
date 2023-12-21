
def find_primes_between_indices(num_list):
    primes = []
    for i in range(11, 12):
        if num_list[i] > 1:
            for j in range(2, num_list[i]):
                if (num_list[i] % j) == 0:
                    break
            else:
                primes.append(num_list[i])
    return sorted(primes)
