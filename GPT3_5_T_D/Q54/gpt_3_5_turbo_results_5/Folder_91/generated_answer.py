
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

def all_right_truncatable_prime(numbers):
    x = numbers[0]
    right_truncatable_primes = []

    for num in range(x - 1, 0, -1):
        if is_prime(num):
            truncatable = True
            digit_count = len(str(num))

            for i in range(digit_count - 1, 0, -1):
                truncated_num = int(str(num)[:i])
                if not is_prime(truncated_num):
                    truncatable = False
                    break

            if truncatable:
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
