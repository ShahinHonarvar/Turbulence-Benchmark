
def return_binary_or_hexa(tuple):
    a = tuple[1]
    b = tuple[8]
    total_sum = sum(range(a+1, b))
    missing_numbers = [num for num in range(a+1, b) if num not in tuple[1:9]]
    if missing_numbers == []:
        return ''
    else:
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:]
