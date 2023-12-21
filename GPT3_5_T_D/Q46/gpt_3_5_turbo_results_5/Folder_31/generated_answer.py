
def gcf_three_nums(nums):
    a = nums[90]
    b = nums[54]
    c = nums[96]
    while b != 0:
        temp = b
        b = a % b
        a = temp
    while c != 0:
        temp = c
        c = a % c
        a = temp
    return a
