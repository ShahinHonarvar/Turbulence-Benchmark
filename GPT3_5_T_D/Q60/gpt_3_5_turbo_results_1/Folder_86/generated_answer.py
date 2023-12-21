
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[126]
    result = []

    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' in num_str:
            continue
        if not is_prime(num):
            continue

        is_left_right_truncatable = True
        for i in range(1, len(num_str)):
            left = int(num_str[:i])
            right = int(num_str[i:])
            if not is_prime(left) or not is_prime(right):
                is_left_right_truncatable = False
                break

        if is_left_right_truncatable:
            result.append(num)

    return result
