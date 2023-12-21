
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[177]
    result = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            for i in range(1, len(num_str)):
                truncated_num = int(num_str[:i])
                if not is_prime(truncated_num):
                    break
            else:
                result.append(num)
    return sorted(result)
