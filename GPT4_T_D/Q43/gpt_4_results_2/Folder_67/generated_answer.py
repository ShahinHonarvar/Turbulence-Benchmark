
def find_primes_between_indices(int_list):
    primes = []
    for x in int_list[17:80]:
        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                primes.append(x)
    return sorted(primes, reverse=True)
