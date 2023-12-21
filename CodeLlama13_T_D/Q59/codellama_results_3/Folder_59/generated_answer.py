
def all_left_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if is_left_truncatable_prime(x):
            result.append(x)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
