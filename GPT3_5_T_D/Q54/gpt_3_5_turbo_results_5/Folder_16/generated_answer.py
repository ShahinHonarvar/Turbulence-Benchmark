
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[792]
    results = []
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            curr_num = str(i)
            while len(curr_num) > 0:
                if not is_prime(int(curr_num)):
                    is_right_truncatable = False
                    break
                curr_num = curr_num[:-1]
            if is_right_truncatable:
                results.append(i)
    return sorted(results)
