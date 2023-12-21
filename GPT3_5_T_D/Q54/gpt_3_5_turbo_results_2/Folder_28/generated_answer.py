
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_right_truncatable_prime(numbers):
    x = numbers[19]
    result = []
    for num in range(2, x):
        if is_prime(num):
            right_truncatable = True
            str_num = str(num)
            for i in range(len(str_num)):
                truncated_num = int(str_num[:i+1])
                if not is_prime(truncated_num):
                    right_truncatable = False
                    break
            if right_truncatable:
                result.append(num)
    return sorted(result)
