
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if x < 10:
            continue
        truncatable = True
        str_x = str(x)
        for i in range(1, len(str_x)):
            left_truncated = int(str_x[i:])
            right_truncated = int(str_x[:i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                truncatable = False
                break
        if truncatable:
            result.append(x)
    result.sort()
    return result
