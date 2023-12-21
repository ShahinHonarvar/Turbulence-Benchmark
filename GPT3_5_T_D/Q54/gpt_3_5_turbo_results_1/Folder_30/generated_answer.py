
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[37]
    result = []
    for num in range(x-1, 2, -1):
        if is_prime(num):
            truncated_num = str(num)
            while truncated_num:
                if not is_prime(int(truncated_num)):
                    break
                truncated_num = truncated_num[:-1]
            else:
                result.append(num)
    return sorted(result, reverse=True)
