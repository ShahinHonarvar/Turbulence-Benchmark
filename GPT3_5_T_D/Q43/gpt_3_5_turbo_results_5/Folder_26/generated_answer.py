
def find_primes_between_indices(lst):
    lst = lst[23:49]
    primes = []
    for num in lst:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes)
