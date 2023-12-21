
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[992]
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            flag = True
            num = str(i)
            while len(num) > 1:
                num = num[1:]
                if not is_prime(int(num)):
                    flag = False
                    break
            if flag:
                result.append(i)
    return result
