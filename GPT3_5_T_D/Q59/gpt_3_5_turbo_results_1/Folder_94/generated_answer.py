
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[43]
    results = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[i:])):
                truncatable = False
                break
        if truncatable:
            results.append(num)
    return sorted(results)
