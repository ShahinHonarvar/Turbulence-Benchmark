
def return_binary_or_hexa(numbers):
    a, b = numbers[1], numbers[8]
    missing_nums = [i for i in range(a+1, b) if i not in numbers[1:9]]
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
