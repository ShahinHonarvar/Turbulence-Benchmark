
def all_left_right_truncatable_prime(t):
    x = t[35]
    primes = []
    def is_prime(n):
        if n < 2:
            return False
        for k in range(2, int(n ** 0.5) + 1):
            if n % k == 0:
                return False
        return True

    def check(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    for num in range(2, x + 1):
        if is_prime(num) and check(num):
            primes.append(num)

    primes.sort(reverse=True)
    return primes
