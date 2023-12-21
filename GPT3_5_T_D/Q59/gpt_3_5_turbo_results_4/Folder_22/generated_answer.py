
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[85]
    result = []
    for i in range(11, x):
        truncatable = True
        for j in range(len(str(i))):
            if str(i)[j] == '0' or not is_prime(int(str(i)[j:])):
                truncatable = False
                break
        if truncatable:
            result.append(i)
    return sorted(result)
