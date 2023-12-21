
def prime_factors(numbers):
    return set([i for i in range(2, int(numbers[3])+1) if all(numbers[3] % i != 0 for j in range(2, int(numbers[3])**0.5+1) if j != i)])
