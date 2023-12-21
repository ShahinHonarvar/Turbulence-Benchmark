
def find_primes_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([ele for ele in lst[112:362] if is_prime(ele)], reverse=True)
