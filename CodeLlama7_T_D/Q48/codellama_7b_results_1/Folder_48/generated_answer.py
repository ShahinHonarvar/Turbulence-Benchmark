 def return_binary_or_hexa(tuple):
    a = tuple[933]
    b = tuple[996]
    sum = 0
    for i in range(a + 1, b - 1 + 1):
        if not tuple.__contains__(i):
            sum += i

    if sum % 2 == 0:
        return hex(sum).upper().replace("0X", "")[::-1]

    else:
        return bin(sum)[2:].zfill(len(bin(sum)) - 2)
