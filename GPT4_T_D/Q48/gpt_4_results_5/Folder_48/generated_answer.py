
def return_binary_or_hexa(tuple_of_numbers):
    a = tuple_of_numbers[933]
    b = tuple_of_numbers[996]
    missing_nums = [i for i in range(a + 1, b) if i not in tuple_of_numbers[933:997]]
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ""
    elif num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]
