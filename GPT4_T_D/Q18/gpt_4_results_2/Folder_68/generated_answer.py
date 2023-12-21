
def sum_ints_div_by_either_nums(int_list):
    try:
        sliced_list = int_list[7:8]
        result = sum([i for i in sliced_list if i % 5 == 0 or i % 7 == 0])
        return result
    except IndexError as e:
        return 0
