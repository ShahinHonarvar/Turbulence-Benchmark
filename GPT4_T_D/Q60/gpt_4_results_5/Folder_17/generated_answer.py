
def all_left_right_truncatable_prime(tup):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def is_left_right_truncatable(n):
        n_str = str(n)
        if '0' in n_str: return False
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:len(n_str)-i])):
                return False
        return True

    x = tup[36]
    return sorted([i for i in range(10, x+1) if is_left_right_truncatable(i)], reverse=True)
