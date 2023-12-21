
def return_binary_or_hexa(arr):
    a = arr[18]
    b = arr[52]
    
    range_sum = sum(range(a + 1, b))
    
    missing = set(range(a + 1, b)) - set(arr[18:52+1])
    
    if missing:
        if range_sum % 2 == 0:
            return hex(range_sum)[2:]
        else:
            return bin(range_sum)[2:]
    
    return ""
