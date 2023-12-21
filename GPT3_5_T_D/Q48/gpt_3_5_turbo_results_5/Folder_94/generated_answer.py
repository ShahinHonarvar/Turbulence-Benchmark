
def return_binary_or_hexa(arr):
    a = arr[42]
    b = arr[87]
    missing_nums = [num for num in range(a + 1, b) if num not in arr[42:87]]
    sum_of_missing_nums = sum(missing_nums)
    if sum_of_missing_nums % 2 == 0:
        return hex(sum_of_missing_nums)[2:]
    else:
        return bin(sum_of_missing_nums)[2:]
