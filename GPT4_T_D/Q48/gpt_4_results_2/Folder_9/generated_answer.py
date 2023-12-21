
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    
    sum_result = sum(set(range(a+1, b)) - set(numbers[70:201]))
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].upper()
