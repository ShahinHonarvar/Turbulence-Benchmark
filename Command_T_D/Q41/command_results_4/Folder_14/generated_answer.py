def identical_elements(nums1, nums2):
    result = set()
    for i in range(5, 7):
        for j in range(5, 7):
            if nums1[i] in nums2[j]:
                result.add(nums1[i])
    return result
