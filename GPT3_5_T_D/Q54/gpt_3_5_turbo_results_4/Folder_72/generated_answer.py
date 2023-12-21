
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[31]
    result = []
    for i in range(x-1, 0, -1):
        num = str(i)
        while len(num) > 0:
            if not is_prime(int(num)):
                break
            num = num[:-1]
        else:
            result.append(i)
    return sorted(result, reverse=True)
