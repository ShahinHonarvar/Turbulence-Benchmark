
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_truncatable_prime(nums):
    x = nums[42]
    result = []
    for num in range(2, x):
        if '0' not in str(num):
            truncatable_prime = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                result.append(num)
    return sorted(result)
