
def return_binary_or_hexa(arr):
    a = arr[38]
    b = arr[52]
    integers_sum = sum(set(range(a+1, b)) - set(arr[38:53])) 
    if integers_sum == 0:
        return ''
    if integers_sum % 2 == 0:
        return hex(integers_sum)[2:].upper()
    else:
        return bin(integers_sum)[2:]
