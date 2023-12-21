
def all_left_truncatable_prime(numbers):
    result = []
    for x in numbers:
        for i in range(1, len(str(x)) + 1):
            n = int(str(x)[:i])
            if is_prime(n) and '0' not in str(n):
                result.append(n)
    return sorted(result, reverse=True)
