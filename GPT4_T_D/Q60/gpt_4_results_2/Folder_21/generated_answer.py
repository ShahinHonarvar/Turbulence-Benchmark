
def is_prime(n):
    if n < 2:
        return False
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        return all(is_prime(int(str_n[i:])) and is_prime(int(str_n[:i+1])) for i in range(len(str_n)))

    x = t[175]
    return sorted(n for n in range(x + 1) if '0' not in str(n) and is_left_right_truncatable_prime(n))
