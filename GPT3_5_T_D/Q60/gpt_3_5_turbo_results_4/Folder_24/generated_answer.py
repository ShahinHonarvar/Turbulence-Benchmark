
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if x < 10:
            continue
        if not is_prime(x):
            continue
        str_x = str(x)
        if '0' in str_x:
            continue
        truncatable = True
        for i in range(1, len(str_x)):
            if not is_prime(int(str_x[i:])) or not is_prime(int(str_x[:i])):
                truncatable = False
                break
        if truncatable:
            result.append(x)
    return sorted(result, reverse=True)
