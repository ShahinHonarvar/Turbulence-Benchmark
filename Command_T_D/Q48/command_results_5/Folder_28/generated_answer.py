
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[86], sorted(nums)[99]
    if a == b:
        return ''
    s = sum(range(a + 1, b, 2))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return '0b' + '{:b}'.format(s)
