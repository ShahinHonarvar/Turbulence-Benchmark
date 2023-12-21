
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    sum_absent = sum(set(range(a + 1, b)) - set(numbers[70:201]))
    
    if sum_absent == 0:
        return ''
    
    if sum_absent % 2 == 0:
        return hex(sum_absent)[2:]
    else:
        return bin(sum_absent)[2:]
