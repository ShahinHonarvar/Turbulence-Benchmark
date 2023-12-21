
def return_binary_or_hexa(arr):
    int_set = set(arr[45:49])
    a = arr[45]
    b = arr[48]
    sum_ = sum(i for i in range(a + 1, b) if i not in int_set)
    if sum_ == 0:
        return ''
    elif sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
