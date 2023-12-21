
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_all_left_right_truncations(num):
    truncations = []
    num_str = str(num)
    for i in range(1, len(num_str)):
        truncations.append(int(num_str[i:]))
        truncations.append(int(num_str[:i]))
    return truncations

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_prime(num):
            truncations = get_all_left_right_truncations(num)
            if all(is_prime(truncation) for truncation in truncations):
                result.append(num)
    return sorted(result, reverse=True)
