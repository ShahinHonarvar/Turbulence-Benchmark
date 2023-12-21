
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[758]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_truncatable_prime = True
        num_str = str(num)
        while num_str != '':
            if not is_prime(int(num_str)):
                is_truncatable_prime = False
                break
            num_str = num_str[1:]
        if is_truncatable_prime:
            result.append(num)
    return result
