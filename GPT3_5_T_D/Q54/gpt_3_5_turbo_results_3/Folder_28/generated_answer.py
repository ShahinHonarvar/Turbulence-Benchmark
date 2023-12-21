
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_right_truncatable_prime(numbers):
    x = numbers[19]
    result = []
    for num in range(2, x):
        if is_prime(num):
            temp_num = num
            while temp_num > 10:
                temp_num //= 10
                if not is_prime(temp_num):
                    break
            else:
                result.append(num)
    return sorted(result)
