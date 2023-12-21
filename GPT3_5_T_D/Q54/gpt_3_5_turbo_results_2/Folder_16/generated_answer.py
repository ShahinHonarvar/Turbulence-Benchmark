
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
    x = numbers[792]
    result = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[:-i])):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return sorted(result)
