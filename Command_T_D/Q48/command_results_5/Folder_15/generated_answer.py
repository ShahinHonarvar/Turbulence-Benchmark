
def return_binary_or_hexa(nums):
    lst = list(range(nums[0] + 1, nums[4] - 1))
    if not set(lst).issubset(set(nums)):
        return bin(sum(lst)).zfill(len(lst)).decode("utf-8")
    return hex(sum(lst)).zfill(len(lst)).decode("utf-8")
