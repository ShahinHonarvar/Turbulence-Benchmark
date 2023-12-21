def identical_elements(nums1, nums2):
    return set(nums1 + nums2).intersection(nums1, nums2)
