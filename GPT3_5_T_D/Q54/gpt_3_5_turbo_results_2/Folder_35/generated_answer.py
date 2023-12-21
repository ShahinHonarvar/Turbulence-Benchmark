
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[177]
    result = []
    for i in range(2, x):
        if is_prime(i):
            is_truncatable = True
            num = str(i)
            while num:
                if not is_prime(int(num)):
                    is_truncatable = False
                    break
                num = num[:-1]
            if is_truncatable:
                result.append(i)
    return sorted(result)
