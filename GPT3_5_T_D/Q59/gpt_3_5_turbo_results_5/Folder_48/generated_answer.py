
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[835]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncatable = True
        curr_num = i
        while curr_num > 10:
            curr_num = int(str(curr_num)[1:])
            if not is_prime(curr_num):
                truncatable = False
                break
        if truncatable:
            result.append(i)
    return sorted(result)
