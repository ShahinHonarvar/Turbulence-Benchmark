
def find_primes_between_indices(lst):
    primes = []
    for num in lst[31:93]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
