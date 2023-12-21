
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[89]
    result = []
    for num in range(x - 1, 0, -1):
        if is_prime(num):
            str_num = str(num)
            is_truncatable_prime = True
            for i in range(len(str_num) - 1):
                trunc_num = int(str_num[:i+1])
                if not is_prime(trunc_num):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(num)
    return sorted(result, reverse=True)
