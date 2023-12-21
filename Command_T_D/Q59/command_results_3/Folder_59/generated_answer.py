import math
def all_left_truncatable_prime(n):
    # your code here
    # n = (n,)
    # lst = []
    # x = n[0]
    # for i in range(2, int(math.sqrt(x)) + 1):
    #     if i * 10 <= x:
    #         lst += range(2, x // 10 + 1)
    #         break
    # lst += range(2, x // 10 + 1)
    # lst = [x//10]
    # lst += range(2, x//10+1)
    # lst += range(x//10, x//5 + 1)
    # lst += range(x//5, x//2 + 1)
    # lst += range(x//2, x//1 + 1)
    # return sorted(lst, reverse=True)
    # return [x//10]
    # return range(x//10, x//5 + 1)
    # return range(x//5, x//2 + 1)
    # return range(x//2, x//1 + 1)
    return [x//10]
    # return range(2, x//10 + 1)
    # return range(2, x//10)
    # return range(x//10, x//5 + 1)
    # return range(x//5, x//2 + 1)
    # return range(x//2, x//1 + 1)
