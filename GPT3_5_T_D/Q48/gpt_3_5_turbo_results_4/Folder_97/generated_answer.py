
def return_binary_or_hexa(tup):
    a = tup[34]
    b = tup[69]
    num_list = list(range(a+1, b))
    missing_nums = [num for num in num_list if num not in tup[34:70]]
    sum_result = sum(missing_nums)

    if sum_result % 2 == 0:
        return hex(sum_result)[2:]
    else:
        return bin(sum_result)[2:]
