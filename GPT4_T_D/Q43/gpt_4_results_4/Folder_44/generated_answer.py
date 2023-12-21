
def find_primes_between_indices(int_list):
    primes = []
    for num in int_list[19:86]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
