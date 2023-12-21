
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[55]
    results = []
    for i in range(2, x):
        if is_prime(i):
            is_truncatable = True
            num_str = str(i)
            for j in range(len(num_str)-1, 0, -1):
                if not is_prime(int(num_str[:j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                results.append(i)
    return sorted(results, reverse=True)
