
def all_left_right_truncatable_prime(t):
    x = t[758]
    
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if "0" in str_n[i:] or not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    result = []
    for i in range(11, x + 1):
        if is_prime(i) and is_truncatable(i):
            result.append(i)

    return sorted(result)
