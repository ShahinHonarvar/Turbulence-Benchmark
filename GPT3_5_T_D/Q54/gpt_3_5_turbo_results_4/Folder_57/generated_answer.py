
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[54]
    result = []

    for i in range(x-1, 1, -1):
        if is_prime(i):
            temp = str(i)
            while len(temp) > 0:
                if not is_prime(int(temp)):
                    break
                temp = temp[:-1]
            else:
                result.append(i)
    return sorted(result, reverse=True)
