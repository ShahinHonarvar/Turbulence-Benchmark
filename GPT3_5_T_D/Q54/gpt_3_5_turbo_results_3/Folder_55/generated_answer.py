
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[73]
    right_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            truncated_number = i
            while truncated_number > 0:
                if not is_prime(truncated_number):
                    break
                truncated_number = truncated_number // 10
            if truncated_number == 0:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
