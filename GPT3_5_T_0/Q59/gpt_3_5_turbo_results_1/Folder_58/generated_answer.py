
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[975]
    result = []
    for i in range(x-1, 1, -1):
        if '0' not in str(i):
            truncatable = True
            for j in range(len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True)
