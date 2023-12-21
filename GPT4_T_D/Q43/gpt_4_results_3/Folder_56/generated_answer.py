
def find_primes_between_indices(arr):
    primes = []
    for i in arr[40:69]:
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                primes.append(i)
    primes.sort(reverse=True)
    return primes
