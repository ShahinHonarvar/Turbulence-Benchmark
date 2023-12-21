import functools
import heapq
@functools.lru_cache(maxsize=1_000_000)
def calc_factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
@functools.lru_cache(maxsize=1_000_000)
def calc_inv_factorial(n):
    res = 1
    for i in range(1, n + 1):
        res /= i
    return res
@functools.lru_cache(maxsize=1_000_000)
def calc_sub_factorial(n, m):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
@functools.lru_cache(maxsize=1_000_000)
def calc_sub_inv_factorial(n, m):
    res = 1
    for i in range(1, n + 1):
        res /= i
    return res
def lists_with_product_equal_n(nums):
    results = []
    # The product of a sublist is the product of all the elements in the sublist.
    # The product of a sublist is the product of all the elements in the sublist.
    # The product of a sublist is the product of all the elements in the sublist.
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                for l in range(k, len(nums)):
                    for m in range(l, len(nums)):
                        if calc_factorial(nums[i-1]) * calc_factorial(nums[j-1]) * calc_factorial(nums[k-1]) * calc_factorial(nums[l-1]) * calc_factorial(nums[m-1]) == calc_factorial(nums[i-1]) * calc_factorial(nums[j-1]) * calc_factorial(nums[k-1]) * calc_factorial(nums[l-1]) * calc_factorial(nums[m-1]):
                            results.append(nums[i-1:j])
                            results.append(nums[j:k])
                            results.append(nums[k:l])
                            results.append(nums[l:m])
                            results.append(nums[m:])
                            break
    return results
