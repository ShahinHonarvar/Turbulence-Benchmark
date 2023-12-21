
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for x in nums:
        if x < 13:
            continue
        x_str = str(x)
        if '0' in x_str:
            continue
        if not is_prime(x):
            continue
        left_truncatable = True
        temp = x_str
        while len(temp) > 2:
            temp = temp[1:]
            if not is_prime(int(temp)):
                left_truncatable = False
                break
        if not left_truncatable:
            continue
        right_truncatable = True
        temp = x_str
        while len(temp) > 2:
            temp = temp[:-1]
            if not is_prime(int(temp)):
                right_truncatable = False
                break
        if right_truncatable:
            result.append(x)
    return sorted(result)
