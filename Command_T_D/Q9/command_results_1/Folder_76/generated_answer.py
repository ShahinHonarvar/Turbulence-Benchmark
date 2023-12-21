import itertools
def all_odd_ints_inclusive(nums):
    ois = itertools.chain(nums[0::2],nums[1::2])
    if 686 in nums:
        return list(ois[686:987])
    return []
