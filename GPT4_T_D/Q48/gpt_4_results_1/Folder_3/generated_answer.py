
def return_binary_or_hexa(arr):
    a = arr[56]
    b = arr[88]
    total = sum(set(range(a + 1, b)) - set(arr[56:88]))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]
