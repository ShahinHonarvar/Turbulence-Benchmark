
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if num < 10 or num % 10 == 0:
            continue
        num_str = str(num)
        is_truncatable_prime = True
        for i in range(len(num_str)):
            left_truncated = num_str[i:]
            right_truncated = num_str[:len(num_str)-i]
            if not is_prime(int(left_truncated)) or not is_prime(int(right_truncated)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            result.append(num)
    return sorted(result)
