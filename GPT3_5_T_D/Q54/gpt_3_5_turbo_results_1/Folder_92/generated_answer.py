
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[7]
    result = []
    for i in range(2, x):
        if is_prime(i):
            trunc_prime = True
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    trunc_prime = False
                    break
                temp //= 10
            if trunc_prime:
                result.append(i)
    return sorted(result)
