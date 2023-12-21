
def prime_factors(my_list):
    return set(get_prime_factors(my_list[59]))

def get_prime_factors(n):
    if n <= 1:
        return []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return [i] + get_prime_factors(n//i)
    return [n]
