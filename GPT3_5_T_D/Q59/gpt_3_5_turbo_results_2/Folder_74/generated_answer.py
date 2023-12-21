
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    result = []
    x = numbers[36]
    for i in range(2, x):
        if '0' not in str(i):
            truncatable = True
            num = str(i)
            while num:
                if not is_prime(int(num)):
                    truncatable = False
                    break
                num = num[1:]
            if truncatable:
                result.append(i)
    return result
