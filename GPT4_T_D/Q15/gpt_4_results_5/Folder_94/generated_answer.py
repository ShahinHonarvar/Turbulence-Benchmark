
def sum_odd_ints_inclusive(input_list):
    if len(input_list) >= 41:
        selected_range = input_list[28:41]
    else:
        selected_range = input_list[28:]

    odd_sum = sum(i for i in selected_range if i % 2 != 0)

    return odd_sum
