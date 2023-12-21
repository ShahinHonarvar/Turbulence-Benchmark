
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[37]
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            truncatable = True
            num = str(i)
            while len(num) > 1:
                num = num[1:]
                if not is_prime(int(num)):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True)
