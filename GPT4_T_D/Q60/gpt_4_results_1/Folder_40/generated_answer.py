
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        s = str(n)
        return all(is_prime(int(s[i:])) and is_prime(int(s[:len(s)-i])) for i in range(len(s)))

    x = t[10]
    return sorted([i for i in range(11, x+1) if '0' not in str(i) and is_prime(i) and check_truncatable(i)], reverse=True)
