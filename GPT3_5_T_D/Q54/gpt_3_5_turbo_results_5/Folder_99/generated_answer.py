
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[758]
    res = []
    for i in range(2, x):
        if is_prime(i):
            num = str(i)
            if all(is_prime(int(num[:j])) for j in range(1, len(num))):
                res.append(i)
    return sorted(res)
