
def all_left_truncatable_prime(tup):
    x = tup[67]
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i: continue
            return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n): return False
        return all(is_prime(int(str(n)[i:])) for i in range(len(str(n))))

    return sorted([i for i in range(x) if is_left_truncatable_prime(i)], reverse=True)
