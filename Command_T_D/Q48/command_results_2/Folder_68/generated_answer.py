
def return_binary_or_hexa(nums):
    a, b = nums[0], nums[-1]
    if a > b:
        return ""
    if a % 2 == 1:
        return "0b" + ("0" * (len(str(a)) - 1) + str(b - a))
    return "0x" + ("0" * (len(str(a)) - 1) + str(b - a))
