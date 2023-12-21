
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    results = []
    x = numbers[6]
    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            truncated = num
            while truncated > 0:
                if not is_prime(truncated):
                    truncatable = False
                    break
                truncated //= 10
            if truncatable:
                results.append(num)

    return sorted(results, reverse=True)
