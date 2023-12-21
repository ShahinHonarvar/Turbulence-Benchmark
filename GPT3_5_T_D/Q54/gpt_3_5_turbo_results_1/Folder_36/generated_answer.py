
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[992]
    result = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            while num_str:
                if not is_prime(int(num_str)):
                    break
                num_str = num_str[:-1]
            else:
                result.append(num)
    return sorted(result)
