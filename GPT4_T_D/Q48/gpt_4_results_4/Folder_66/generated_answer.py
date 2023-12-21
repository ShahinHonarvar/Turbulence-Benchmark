
def return_binary_or_hexa(my_tuple):
    a = my_tuple[11]
    b = my_tuple[76]
    total_sum = 0

    for num in range(a + 1, b):
        if num not in my_tuple[11:77]:
            total_sum += num
            
    if total_sum == 0:
        return ""

    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
