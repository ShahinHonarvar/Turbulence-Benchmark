
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[8]
    left_truncatable_primes = []
    for num in range(x-1, 1, -1):
        if '0' not in str(num):
            is_left_truncatable_prime = True
            truncated_num = str(num)
            while len(truncated_num) > 1:
                truncated_num = truncated_num[1:]
                if int(truncated_num) not in left_truncatable_primes and not is_prime(int(truncated_num)):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                left_truncatable_primes.append(num)

    return sorted(left_truncatable_primes, reverse=True)
