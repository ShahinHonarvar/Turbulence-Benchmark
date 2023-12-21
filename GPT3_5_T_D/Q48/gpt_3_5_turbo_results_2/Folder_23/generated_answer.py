
def return_binary_or_hexa(arr):
    a = arr[20]
    b = arr[36]
    range_sum = 0
    
    for i in range(a + 1, b):
        if i not in arr[21:36]:
            range_sum += i
    
    if range_sum % 2 == 0:
        return hex(range_sum)[2:]
    else:
        return bin(range_sum)[2:]
