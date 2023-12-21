
def find_primes_between_indices(int_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = []
    
    if len(int_list)<80:
        return prime_list

    for val in int_list[66:80]:
        if is_prime(val):
            prime_list.append(val)
    return sorted(prime_list, reverse=True)
