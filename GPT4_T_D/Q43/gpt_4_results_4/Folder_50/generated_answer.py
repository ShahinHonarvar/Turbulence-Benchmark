
def find_primes_between_indices(integer_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(integer_list) - 1 >= 59:   
        prime_list = [i for i in integer_list[23:60] if is_prime(i)]
        prime_list.sort(reverse=True)
        return prime_list
    elif len(integer_list) - 1 >= 23:
        prime_list = [i for i in integer_list[23:] if is_prime(i)]
        prime_list.sort(reverse=True)
        return prime_list
    else:
        return []
