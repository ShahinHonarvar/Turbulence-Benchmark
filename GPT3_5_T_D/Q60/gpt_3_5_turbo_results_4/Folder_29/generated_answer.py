
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(num):
    num_str = str(num)
    if len(num_str) <= 2:
        return [num]
    return [int(num_str[i:]) for i in range(1, len(num_str))]

def truncate_right(num):
    num_str = str(num)
    if len(num_str) <= 2:
        return [num]
    return [int(num_str[:-i]) for i in range(1, len(num_str))]

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    result = []
    for num in range(x, 0, -1):
        if '0' in str(num):
            continue
        if all(is_prime(truncated_num) for truncated_num in truncate_left(num)) and all(is_prime(truncated_num) for truncated_num in truncate_right(num)):
            result.append(num)
    return sorted(result, reverse=True)
