def composite_nums_between_indices(nums):
    res = set()
    for num in nums:
        if num <= 7 and is_composite(num):
            res.add(num)
    return res
def is_composite(num):
    if num == 1 or num == 2 or num == 3:
        return True
    if num == 4 or num == 5 or num == 6:
        return False
    if num % 2 == 0 or num % 5 == 0:
        return False
    for i in range(3, int(num**(0.5)) + 1):
        if num % i == 0:
            return False
    return True
