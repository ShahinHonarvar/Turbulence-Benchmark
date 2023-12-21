
def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    sum_val = sum(set(range(a+1, b)) - set(numbers[80:201]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()
