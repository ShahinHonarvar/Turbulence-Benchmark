
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[35]
    result = []
    for i in range(x-1, 1, -1):
        truncated = str(i)
        while truncated:
            if not is_prime(int(truncated)):
                break
            truncated = truncated[:-1]
        else:
            result.append(i)
    return sorted(result, reverse=True)
