
def all_left_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_truncatable_prime(n):
    if n < 2 or any('0' in str(i) for i in range(2, int(n ** 0.5) + 1)):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
