def identical_elements(nums1, nums2):
    return set(range(min(i for i, x in enumerate(nums1) if x in nums2[200:]), max(i for i, x in enumerate(nums1) if x in nums2[200:]) + 1))
