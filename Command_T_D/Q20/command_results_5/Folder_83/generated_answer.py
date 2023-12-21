def find_n_th_smallest_num(nums):
    if len(nums) < 300:
        return None
    if len(nums) < 30:
        return nums[len(nums) - 1]
    else:
        m_low = nums[29]
        m_high = nums[300]
        for i in range(m_low, m_high + 1):
            if nums[i] < i:
                return nums[i]
        return nums[m_high]
