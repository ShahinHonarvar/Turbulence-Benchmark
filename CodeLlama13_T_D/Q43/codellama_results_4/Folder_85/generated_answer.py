
def find_primes_between_indices(my_list):
    primes = []
    for i in range(32, 36):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    break
            else:
                primes.append(my_list[i])
    return sorted(primes)
