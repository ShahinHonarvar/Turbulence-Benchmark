 
def find_primes_between_indices(list):
    list = [x for x in list if x >= 14 and x <= 73]
    list = [x for x in list if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]
    return sorted(list)
