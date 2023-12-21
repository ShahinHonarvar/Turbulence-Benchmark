
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(nums):
    x = nums[370]
    result = []
    for num in range(x-1, 0, -1):
        if '0' in str(num):
            continue
        truncated_num = str(num)
        while truncated_num:
            if not is_prime(int(truncated_num)):
                break
            truncated_num = truncated_num[1:]
        else:
            result.append(num)
    return result
