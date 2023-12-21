
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[618]
    result = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            while len(num) > 1:
                num = num[:-1]
                if not is_prime(int(num)):
                    break
            else:
                result.append(i)
    return sorted(result)
