
def return_binary_or_hexa(nums):
    a, b = nums[200], nums[202]
    return ("{:b}".format(sum(nums[a + 1 : b - 1]) % 2), "{:x}".format(sum(nums[a + 1 : b - 1])))
