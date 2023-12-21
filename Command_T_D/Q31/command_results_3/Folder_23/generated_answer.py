import bisect
def if_perfect_num(nums):
    return (bisect.bisect_left(nums,69) != bisect.bisect_right(nums,69))
