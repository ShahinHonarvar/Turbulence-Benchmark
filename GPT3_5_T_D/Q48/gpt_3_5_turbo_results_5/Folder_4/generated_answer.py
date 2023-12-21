
def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]

    sum_nums = 0
    for num in range(a+1, b):
        if num not in numbers[50:74]:
            sum_nums += num

    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]
