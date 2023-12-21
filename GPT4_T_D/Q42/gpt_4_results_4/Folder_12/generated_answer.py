
def prime_factors(int_list):
    num = int_list[27]
    factors = set()
    for i in range(2, num + 1):
        while num % i == 0:
            factors.add(i)
            num /= i
    return factors
