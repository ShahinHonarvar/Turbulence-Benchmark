
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    missing_nums = []
    for i in range(a + 1, b):
        if i not in numbers[13:77]:
            missing_nums.append(i)
    if len(missing_nums) == 0:
        return ""
    else:
        sum_of_missing_nums = sum(missing_nums)
        if sum_of_missing_nums % 2 == 1:
            return bin(sum_of_missing_nums)[2:]
        else:
            return hex(sum_of_missing_nums)[2:]
