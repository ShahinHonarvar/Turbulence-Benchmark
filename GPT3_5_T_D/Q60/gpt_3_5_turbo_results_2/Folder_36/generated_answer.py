
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for x in nums:
        if x < 11:
            continue
        x = str(x)
        if "0" in x:
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(1, len(x)):
            left_trunc = int(x[i:])
            right_trunc = int(x[:len(x)-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            result.append(int(x))
    return sorted(result)
