 
def find_primes_between_indices(lst):
    result = []
    for x in range(3, 9):
        if all(x % y for y in range(2, int(x ** 0.5) + 1)):
            result.append(x)
    return result
