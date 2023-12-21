
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[77], sorted(nums)[84]
    if not a:
        return ""
    if a == b - 1:
        return "0b1"
    return "0b1" if a % 2 else "0o" + str(a + 1) + ">" + str(b - 1)
