
def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    missing = [x for x in range(a + 1, b) if x not in numbers[17:88]]
    if missing:
        sum_missing = sum(missing)
        if sum_missing % 2 == 0:
            return hex(sum_missing)[2:]
        else:
            return bin(sum_missing)[2:]
    else:
        return ''
