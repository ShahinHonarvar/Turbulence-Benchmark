
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def all_right_truncatable_prime(numbers):
    x = numbers[86]
    result = []
    for num in range(x - 1, 10, -1):
        if is_prime(num):
            truncatable = True
            temp = num
            while temp > 10:
                temp //= 10
                if not is_prime(temp):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    result.sort(reverse=True)
    return result
