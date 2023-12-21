
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_truncatable_prime(nums):
    x = nums[89]
    result = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            is_left_truncatable_prime = True
            num_str = str(i)
            while len(num_str) > 1:
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                result.append(i)
    return sorted(result, reverse=True)
