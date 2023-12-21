
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
            if not is_prime(int(num_str[:i+1])):
                return False
        return True

    x = numbers[36]
    truncatable_primes = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)

    return sorted(truncatable_primes, reverse=True)
