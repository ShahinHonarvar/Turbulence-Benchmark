
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n%i == 0:
                return False
        return True
    
    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i])) for i in range(len(str_n), 0, -1))

    x = tup[46]
    result = [i for i in range(x) if is_right_truncatable_prime(i)]
    result.sort(reverse=True)
    return result
