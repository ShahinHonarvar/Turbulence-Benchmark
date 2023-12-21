
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[618]
    results = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncatable = True
        num = str(i)
        while truncatable and len(num) > 1:
            num = num[1:]
            if not is_prime(int(num)):
                truncatable = False
        if truncatable:
            results.append(i)
    return results
