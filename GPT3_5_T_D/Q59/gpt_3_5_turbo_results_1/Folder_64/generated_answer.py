
def all_left_truncatable_prime(t):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    x = t[4]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num):
            temp = str(num)
            truncatable = True
            while len(temp) > 0:
                if not is_prime(int(temp)):
                    truncatable = False
                    break
                temp = temp[1:]
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
