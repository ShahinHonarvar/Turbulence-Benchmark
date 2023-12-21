
def all_left_right_truncatable_prime(numbers):
    result = []
    for n in numbers:
        if is_left_and_right_truncatable_prime(n):
            result.append(n)
    return sorted(result)

def is_left_and_right_truncatable_prime(n):
    if n < 10 or n % 11 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
