def lists_with_product_equal_n(int_list):
    result = []
    for i in range(1, len(int_list)):
        curr_list = [int_list[i]]
        while curr_list:
            curr_list = []
            for j in range(1, len(curr_list)):
                curr_list += [curr_list[-1]]
                if curr_list[0] * curr_list[-1] == 48:
                    result += [curr_list]
                    break
            if curr_list[0] * curr_list[-1] == 48:
                break
    return result
