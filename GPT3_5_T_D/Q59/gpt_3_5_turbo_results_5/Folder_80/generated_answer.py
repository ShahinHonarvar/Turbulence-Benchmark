
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    result = []
    for num in range(x-1, 10, -1):
        if '0' in str(num):
            continue
        is_left_truncatable = True
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(num)
    return result
