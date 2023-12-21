
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[57]
    result = []
    for num in range(x - 1, 0, -1):
        str_num = str(num)
        if '0' not in str_num:
            is_truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    is_truncatable = False
                    break
            if is_truncatable and is_prime(num):
                result.append(num)
    return sorted(result, reverse=True)
