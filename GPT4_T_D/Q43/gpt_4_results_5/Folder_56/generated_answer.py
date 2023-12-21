
def find_primes_between_indices(num_list):
    primes = []
    for i in range(40, 69):
        if i < len(num_list) and num_list[i] > 1:
            for j in range(2, num_list[i]):
                if (num_list[i] % j) == 0:
                    break
            else:
                primes.append(num_list[i])
    return sorted(primes, reverse=True)
