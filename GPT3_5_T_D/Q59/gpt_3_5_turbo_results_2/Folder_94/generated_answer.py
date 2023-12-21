
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[43]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        trunc_prime = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                trunc_prime = False
                break
        if trunc_prime:
            result.append(num)
    return sorted(result)
