
def return_binary_or_hexa(num_tuple):
    a = num_tuple[35]
    b = num_tuple[64]
    total_sum = 0
    for num in range(a+1, b):
        if num not in num_tuple[35:65]:
            total_sum += num
    if total_sum % 2 != 0:
        binary = bin(total_sum)[2:]
        return binary
    else:
        hexadecimal = hex(total_sum)[2:]
        return hexadecimal.upper()
