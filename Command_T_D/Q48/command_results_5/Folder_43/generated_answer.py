
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[10], sorted(nums)[28]
    if a > b:
        return ""
    odd = sum(nums[10:28]) % 2
    if odd:
        return format(odd, "b")
    else:
        return format(sum(nums[10:28]), "x")
