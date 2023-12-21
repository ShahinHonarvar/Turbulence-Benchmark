
def all_left_right_truncatable_prime(values):
    x = values[29]

    def prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        return all(prime(int(str_n[i:])) and prime(int(str_n[:len(str_n)-i])) for i in range(len(str_n)))

    return sorted([n for n in range(10, x+1) if prime(n) and truncatable(n)])
