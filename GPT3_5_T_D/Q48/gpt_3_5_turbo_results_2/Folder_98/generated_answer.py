
def return_binary_or_hexa(arr):
    a = arr[6]
    b = arr[7]
    total_sum = 0
    for i in range(a+1, b):
        if i not in arr[6:8]:
            total_sum += i
    
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
