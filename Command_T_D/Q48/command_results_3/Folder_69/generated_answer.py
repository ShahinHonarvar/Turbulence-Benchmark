
def return_binary_or_hexa(nums):
    a, b = 39, 43
    return ("" if set(range(a + 1, b - 1)).intersection(nums) else
