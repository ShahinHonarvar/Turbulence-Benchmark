
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[3]
    left_truncatable_primes = []

    for num in range(x - 1, 0, -1):
        prime = True
        if '0' not in str(num):
            truncated_num = num
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    prime = False
                    break
                truncated_num //= 10
            if prime:
                left_truncatable_primes.append(num)

    return sorted(left_truncatable_primes, reverse=True)
