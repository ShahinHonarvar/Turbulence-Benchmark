
def gcf(a, b):
    while(b):
        a, b = b, a % b
    return a

def gcf_three_nums(nums):
    index_0 = nums[0]
    index_7 = nums[7]
    index_9 = nums[9]
    gcf_0_7 = gcf(index_0, index_7)
    gcf_0_7_9 = gcf(gcf_0_7, index_9)
    return gcf_0_7_9
