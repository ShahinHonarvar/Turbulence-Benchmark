
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[0]
    result = []
    for num in range(x - 1, 0, -1):
        if '0' in str(num):
            continue
        truncatable = True
        while num > 0:
            if not is_prime(num):
                truncatable = False
                break
            num //= 10
        if truncatable:
            result.append(num)
    return sorted(result, reverse=True)
