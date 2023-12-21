
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(n):
    if n < 10 or n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
