
def prime_factors(my_list):
    return set([factor for num in my_list[0].factors() for factor in num if is_prime(factor)])
