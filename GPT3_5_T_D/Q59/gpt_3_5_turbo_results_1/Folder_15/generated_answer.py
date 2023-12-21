
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[6]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncatable_prime = True
        num = str(i)
        while num:
            if not is_prime(int(num)):
                truncatable_prime = False
                break
            num = num[1:]
        if truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)
