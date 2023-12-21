
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[24]
    right_truncatable_primes = []
    for i in range(2, x):
        num = str(i)
        prime = True
        for j in range(1, len(num)):
            truncated_num = int(num[:-j])
            if not is_prime(truncated_num):
                prime = False
                break
        if prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
