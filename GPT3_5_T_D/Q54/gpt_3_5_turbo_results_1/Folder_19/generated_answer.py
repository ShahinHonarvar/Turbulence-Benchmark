
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = t[67]
    primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            truncated_num = num
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    break
                truncated_num //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
