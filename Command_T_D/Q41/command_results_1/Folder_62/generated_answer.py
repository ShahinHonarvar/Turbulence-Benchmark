def identical_elements(nums1, nums2):
    result = set()
    for i in range(91, 99):
        if nums1[i] in nums2:
            result.add(nums1[i])
        if nums2[i] in nums1:
            result.add(nums2[i])
    return result
