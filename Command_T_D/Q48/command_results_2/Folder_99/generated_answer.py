
def return_binary_or_hexa(nums):
    i = next((i for i in range(427, 669) if nums[i] == 0), None)
    if i is None:
        return ""
    a = nums[i]
    b = nums[i + 1]
    if b - a - 1 % 2:
        return bin(b - a - 1).zfill(b - a - 1).decode("ascii")
    else:
        return hex(b - a - 1).zfill(b - a - 1).decode("ascii")
