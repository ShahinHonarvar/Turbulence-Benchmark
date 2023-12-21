
def return_binary_or_hexa(arr):
    a = arr[62]
    b = arr[96]
    
    missing_nums = [i for i in range(a + 1, b) if i not in arr[62:97]]
    sum_nums = sum(missing_nums)
    
    if not missing_nums:
        return ''
    elif sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
