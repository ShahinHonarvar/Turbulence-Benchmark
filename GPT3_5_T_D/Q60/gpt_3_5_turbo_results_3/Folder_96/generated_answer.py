
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    if '0' in str(num):
        return False
    str_num = str(num)
    length = len(str_num)
    for i in range(length):
        if not is_prime(int(str_num[i:])):
            return False
        if not is_prime(int(str_num[:length-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return result
