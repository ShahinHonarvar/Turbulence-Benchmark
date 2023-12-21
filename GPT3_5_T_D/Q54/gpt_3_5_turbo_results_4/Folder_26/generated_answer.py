
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[81]
    res = []
    for num in range(x-1, 10, -1):
        if is_prime(num):
            truncated_num = num // 10
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    break
                truncated_num //= 10
            else:
                res.append(num)
    return sorted(res, reverse=True)
