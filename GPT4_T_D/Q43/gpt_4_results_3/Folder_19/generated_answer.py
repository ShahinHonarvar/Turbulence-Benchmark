
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True    

    if len(int_list) < 98:
        return []
    else:
        return sorted([num for num in int_list[21:98] if is_prime(num)])
