
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(nums):
    x = nums[97]
    result = []
    for i in range(11, x):
        if '0' not in str(i):
            is_truncatable_prime = True
            for j in range(len(str(i))):
                num = int(str(i)[j:])
                if not is_prime(num):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(i)
    return sorted(result)
