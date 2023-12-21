
def all_left_right_truncatable_prime(t):
    x = t[975]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str)-i])):
                return False
        return True

    truncatable_primes = []
    for num in range(x+1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
