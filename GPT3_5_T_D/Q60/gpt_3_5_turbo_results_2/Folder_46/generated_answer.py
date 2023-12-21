
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
        if not is_prime(int(num_str[:i+1])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[33]
    result = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            result.append(i)
    return result
