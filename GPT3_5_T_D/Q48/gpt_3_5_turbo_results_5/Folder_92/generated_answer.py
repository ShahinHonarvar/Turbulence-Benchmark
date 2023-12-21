
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[2]
    total_sum = sum(numbers[1:b-1]) - sum(numbers[1:a])
  
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum).split('x')[1]
    else:
        return bin(total_sum)[2:]
