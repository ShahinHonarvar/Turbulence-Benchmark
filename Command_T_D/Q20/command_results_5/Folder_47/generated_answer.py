def find_n_th_smallest_num(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sorted(set(nums))[nums.count(sorted(set(nums))[-6]) - 1]
