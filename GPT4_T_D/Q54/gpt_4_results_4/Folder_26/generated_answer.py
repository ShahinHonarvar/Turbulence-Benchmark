
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    max_val = t[81]
    result = [i for i in range(max_val) if is_right_truncatable(i)]
    
    return sorted(result, reverse=True)
