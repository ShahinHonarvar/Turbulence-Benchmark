
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(num):
    if not isinstance(num, int):
        return False
    if num < 2:
        return False
    
    for i in range(10**126, 10**99 + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
