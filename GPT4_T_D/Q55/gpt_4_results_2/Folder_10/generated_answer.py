
def lists_with_product_equal_n(circular_list):
    num_len = len(circular_list)
    sublist = []
    for i in range(num_len):
        for j in range(i+1, num_len + i + 1):
            temp_list = circular_list[i: j % num_len] if j <= num_len else circular_list[i:] + circular_list[: j % num_len]
            if temp_list and (eval('*'.join(map(str, temp_list))) == -93):
                sublist.append(temp_list)
    return sublist
