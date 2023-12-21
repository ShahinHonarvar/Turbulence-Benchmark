
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_truncatable_prime(nums):
    x = nums[100]
    result = []
    for i in range(2, x):
        if is_prime(i):
            is_left_truncatable_prime = True
            num_str = str(i)
            for j in range(1, len(num_str)):
                truncated_num = int(num_str[j:])
                if not is_prime(truncated_num):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                result.append(i)
    return result
