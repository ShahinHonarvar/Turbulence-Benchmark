
def prime_factors(my_list):
    return set(factor for factor in range(2, my_list[42]) if my_list[42] % factor == 0 and is_prime(factor))

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
