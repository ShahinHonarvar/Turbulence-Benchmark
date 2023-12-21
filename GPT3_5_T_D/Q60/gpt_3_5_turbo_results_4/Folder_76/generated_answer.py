
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                return False
        return True

    def is_right_truncatable_prime(n):
        num_str = str(n)
        while len(num_str) > 1:
            num_str = num_str[:-1]
            if not is_prime(int(num_str)):
                return False
        return True

    x = numbers[370]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
