def lists_with_product_equal_n(nums):
    if not nums:
        return []
    ans = []
    while nums:
        if nums[0] == n:
            ans += [nums]
            break
        if nums[0] == n // 2:
            ans += [[nums[0], nums[1]]
            break
        if nums[0] == n // 3:
            ans += [[nums[0], nums[1], nums[2]]
            break
        if nums[0] == n // 4:
            ans += [[nums[0], nums[1], nums[2], nums[3]]
            break
        if nums[0] == n // 5:
            ans += [[nums[0], nums[1], nums[2], nums[3], nums[4]]
            break
        if nums[0] == n // 6:
            ans += [[nums[0], nums[1], nums[2], nums[3], nums[4], nums[5]]
            break
        if nums[0] == n // 7:
            ans += [[nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6]]
            break
        if nums[0] == n // 8:
            ans += [[nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7]]
            break
        if nums[0] == n // 9:
            ans += [[nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8]]
            break
        if nums[0] == n // 10:
            ans += [[nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9]]
            break
    return ans
