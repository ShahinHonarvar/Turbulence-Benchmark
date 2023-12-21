
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[6], sorted(nums)[9]
    if not (b - a - 1).is_odd():
        return hex(b - a - 1)
    else:
        return f'0b{(b - a - 1).bit_length():b}'
