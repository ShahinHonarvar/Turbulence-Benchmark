
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 2:
            if is_prime(n):
                n = int(str(n)[1:-1])
            else:
                return False
        return is_prime(n)

    x = nums[77]
    result = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result
