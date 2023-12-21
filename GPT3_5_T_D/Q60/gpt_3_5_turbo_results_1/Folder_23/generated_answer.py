
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left_right(n):
    digits = str(n)
    truncatables = []
    for i in range(len(digits)):
        left = int(digits[i:])
        right = int(digits[:i+1])
        if is_prime(left) and is_prime(right):
            truncatables.append(int(digits[i:]))
    return truncatables

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and all(is_prime(int(substr)) for substr in str(num)):
            truncatables = truncate_left_right(num)
            if len(truncatables) == 0:
                continue
            if all(is_prime(trunc) for trunc in truncatables):
                result.append(num)
    return sorted(result, reverse=True)
