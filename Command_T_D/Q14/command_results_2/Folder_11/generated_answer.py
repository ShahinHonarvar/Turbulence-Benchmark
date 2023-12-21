def find_second_smallest_num(nums):
    sm, sm2 = sorted(set(nums)[66:93]), sorted(set(nums)[66:93])[-2]
    return next(x for x in sm2 if x < sm)
