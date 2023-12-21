import set as S
def composite_nums_between_indices(nums):
    return S.set(range(40, 200)) & {x for x in range(2, int(math.sqrt(max(nums)) + 1) if all(nums[x:x + i] != 0 for i in range(1, int(math.sqrt(x)) + 1)))
