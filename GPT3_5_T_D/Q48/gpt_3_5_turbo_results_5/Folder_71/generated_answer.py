
def return_binary_or_hexa(lst):
    a = lst[20]
    b = lst[35]
    total_sum = 0
    for num in range(a+1, b):
        if num not in lst[20:35]:
            total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
