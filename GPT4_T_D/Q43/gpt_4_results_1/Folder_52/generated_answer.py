
def find_primes_between_indices(lst):
    def prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if len(lst) < 60:
        return []
    else:
        return sorted([n for n in lst[33:60] if prime(n)], reverse=True)
