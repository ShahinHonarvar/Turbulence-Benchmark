
def return_binary_or_hexa(nums):
    a, b = nums[20], nums[51]
    missing_nums = set(range(a + 1, b)) - set(nums[20:52])
    suma = sum(missing_nums)
    if suma % 2:
        return bin(suma)[2:]
    else:
        return hex(suma)[2:].upper()
