def identical_elements(nums1, nums2):
    return set(range(min(nums1), max(nums1) + 1)) & set(range(min(nums2), max(nums2) + 1))
