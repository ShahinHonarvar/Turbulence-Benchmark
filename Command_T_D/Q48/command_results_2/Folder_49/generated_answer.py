
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[80], sorted(nums)[200]
    odd = sum(range(a + 1, b)) % 2
    return (str(odd).zfill(len(str(odd)) + 2) if odd else
