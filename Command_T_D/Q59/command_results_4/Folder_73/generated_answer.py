def all_left_truncatable_prime(nums):
    lst = [nums[i] for i in range(len(nums)) if nums[i] < 10]
    return sorted(lst)
