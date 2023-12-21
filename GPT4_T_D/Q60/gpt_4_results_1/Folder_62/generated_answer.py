
def all_left_right_truncatable_prime(num_tuple):
    def is_prime(n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i*i <= n:
            if n % i == 0 or n % (i+2) == 0: return False
            i += 6
        return True

    def is_truncatable(n):
        n = str(n)
        return all(is_prime(int(n[i:])) and is_prime(int(n[:i+1])) for i in range(len(n)))

    x = num_tuple[70]
    return sorted(i for i in range(x+1) if "0" not in str(i) and is_prime(i) and is_truncatable(i))
