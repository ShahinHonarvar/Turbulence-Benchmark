
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if num < 10:
            continue
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        digits = len(str_num)
        for i in range(1, digits):
            if not is_prime(int(str_num[i:])):
                is_truncatable = False
                break
        for i in range(digits-1, 0, -1):
            if not is_prime(int(str_num[:i])):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result)
