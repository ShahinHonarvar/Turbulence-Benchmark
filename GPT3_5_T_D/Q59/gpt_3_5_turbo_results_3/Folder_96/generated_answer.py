
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncated = str(i)
        while truncated:
            if not is_prime(int(truncated)):
                break
            truncated = truncated[1:]
        if not truncated:
            result.append(i)
    return result
