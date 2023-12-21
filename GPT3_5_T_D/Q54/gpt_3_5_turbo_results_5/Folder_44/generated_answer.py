
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    result = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            for i in range(1, len(str(num))):
                truncated_num = int(str(num)[:-i])
                if not is_prime(truncated_num):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return sorted(result)
