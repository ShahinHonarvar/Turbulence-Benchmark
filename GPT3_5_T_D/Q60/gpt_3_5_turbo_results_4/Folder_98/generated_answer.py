
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[8]
    result = []

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_truncatable_prime(int(str(n)[1:-1]))

    for i in range(2, x + 1):
        if i not in [2, 3, 5, 7]:
            continue
        if is_truncatable_prime(i):
            result.append(i)

    return sorted(result, reverse=True)
