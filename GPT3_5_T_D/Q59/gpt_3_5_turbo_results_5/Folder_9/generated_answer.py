
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncatable = True
        digits = str(i)
        while len(digits) > 1:
            digits = digits[1:]
            if not is_prime(int(digits)):
                truncatable = False
                break
        if truncatable:
            result.append(i)
    return sorted(result, reverse=True)
