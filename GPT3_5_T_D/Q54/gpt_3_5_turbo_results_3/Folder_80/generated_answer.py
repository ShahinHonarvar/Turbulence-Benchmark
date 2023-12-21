
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[14]
    result = []
    for i in range(x - 1, 10, -1):
        num_str = str(i)
        is_truncatable_prime = True
        for j in range(len(num_str)):
            truncated_num = int(num_str[:j+1])
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)
