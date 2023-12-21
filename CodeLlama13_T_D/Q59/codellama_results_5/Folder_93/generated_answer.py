
def all_left_truncatable_prime(numbers):
    result = []
    for i in range(len(numbers)):
        x = numbers[i]
        if is_left_truncatable_prime(x):
            result.append(x)
    return sorted(result)

def is_left_truncatable_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
