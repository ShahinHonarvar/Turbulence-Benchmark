
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' not in str_n:
            for i in range(len(str_n)):
                left_str = str_n[i:]
                right_str = str_n[:len(str_n)-i]
                if not (is_prime(int(left_str)) and is_prime(int(right_str))):
                    return False
            return True
        return False

    x = t[70]
    return sorted([i for i in range(11, x+1) if is_truncatable_prime(i)], reverse=True)
