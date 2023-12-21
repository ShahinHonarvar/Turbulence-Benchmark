
def all_right_truncatable_prime(t):
    x = t[1]

    def check_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def check_right_truncatable(num):
        num = str(num)
        while len(num) > 0:
            if not check_prime(int(num)):
                return False
            num = num[:-1]
        return True

    primes = []
    for num in range(2, x):
        if check_right_truncatable(num):
            primes.append(num)
    primes.sort(reverse=True)

    return primes
