
def all_left_right_truncatable_prime(t):
    x = t[97]
    primes = []
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_left_right_trun_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i+1])):
                return False
        return True

    for i in range(10, x + 1):
        if '0' not in str(i) and is_prime(i) and is_left_right_trun_prime(i):
            primes.append(i)
    return sorted(primes)
