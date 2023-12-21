
def return_binary_or_hexa(tup) -> str:
    a = tup[3]
    b = tup[8]
    numbers = set(range(a + 1, b))
    tuple_nums = set(tup[3:8])
    missing_nums = numbers - tuple_nums
    total_sum  = sum(missing_nums)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
