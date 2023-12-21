
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(n):
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
