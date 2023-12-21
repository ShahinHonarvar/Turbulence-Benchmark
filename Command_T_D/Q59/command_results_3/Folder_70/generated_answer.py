import sys
def all_left_truncatable_prime(nums):
    #sys.setrecursionlimit(10**6)
    res = []
    for i in range(len(str(nums[0]))):
        for j in range(len(str(nums[0]))-1, -1, -1):
            if nums[0][i] != '0':
                break
            else:
                temp = int(str(nums[0])[:j])
                if temp == nums[0]:
                    break
                elif temp in res:
                    break
                elif is_prime(temp):
                    res += [temp]
    return res
def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    maxDivisor = int(x ** .5) + 1
    if x % maxDivisor == 0:
        return False
    return all(x % i != 0 for i in range(maxDivisor, x // 2 + 1))
