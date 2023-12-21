
def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]

    sum = 0
    set_nums = set(numbers[69:98])
    for i in range(a + 1, b):
        if not i in set_nums:
            sum += i

    if sum == 0:
        return ""
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
