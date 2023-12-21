
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[175]
    result = []
    for n in range(2, x):
        truncated = str(n)
        while is_prime(int(truncated)):
            truncated = truncated[:-1]
            if truncated == '':
                result.append(n)
                break
    return sorted(result)
