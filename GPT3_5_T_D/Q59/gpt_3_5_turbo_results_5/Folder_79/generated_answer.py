
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[91]
    result = []

    for i in range(11, x):
        if '0' not in str(i) and all(is_prime(int(str(i)[j:])) for j in range(len(str(i)))):
            result.append(i)

    return sorted(result)
