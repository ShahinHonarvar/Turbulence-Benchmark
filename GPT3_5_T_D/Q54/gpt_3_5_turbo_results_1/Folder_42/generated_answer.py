
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[64]
    results = []
    for i in range(x-1, 1, -1):
        if is_prime(i):
            num = str(i)
            truncatable = True
            while truncatable and num != '':
                if not is_prime(int(num)):
                    truncatable = False
                num = num[:-1]
            if truncatable:
                results.append(i)
    return sorted(results, reverse=True)
