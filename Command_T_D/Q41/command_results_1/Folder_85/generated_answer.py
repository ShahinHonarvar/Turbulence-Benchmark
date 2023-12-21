def identical_elements(nums1, nums2):
    result = set()
    for i in range(len(nums1)-5, len(nums1)-3):
        if nums1[i] in nums2[i+5:i-3]:
            result.add(nums1[i])
    return result
